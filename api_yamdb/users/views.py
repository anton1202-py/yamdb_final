from smtplib import SMTPResponseException

from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import response, status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from users.models import User
from users.permissions import AdminPermissions
from users.serializers import (AdminUserSerializer, AuthentificationSerializer,
                               RegistrationSerializer, UserSerializer)


@api_view(['POST'])
@permission_classes([AllowAny])
def signup_view(request):
    serializer = RegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data.get('username')
    email = serializer.validated_data.get('email')
    user, _ = User.objects.get_or_create(username=username,
                                         email=email)
    code = default_token_generator.make_token(user)
    try:
        send_mail(
            'Token',
            f'{code}',
            f'{settings.MAILING_EMAIL}',
            [email]
        )
        response.Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )
    except SMTPResponseException:
        return response.Response(
            data={'error': "Не получилось отправить эмейл"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['POST'])
@permission_classes([AllowAny])
def confirmation_view(request):
    serializer = AuthentificationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    code = serializer.validated_data.get('confirmation_code')
    username = serializer.validated_data.get('username')
    user = get_object_or_404(User, username=username)
    if not default_token_generator.check_token(user, code):
        return response.Response(
            data={'error': 'некорректный код подтверждения'},
            status=status.HTTP_400_BAD_REQUEST
        )
    token = user.token
    return response.Response(
        data={'access': str(token)},
        status=status.HTTP_200_OK
    )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = (AdminPermissions,)
    lookup_field = 'username'

    @action(
        detail=False,
        methods=['GET', 'PATCH'],
        permission_classes=(IsAuthenticated,)
    )
    def me(self, request):
        if request.method == 'GET':
            serializer = UserSerializer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = UserSerializer(
            request.user, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
