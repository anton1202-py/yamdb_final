![Github CI/CD](https://github.com/anton1202-py/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# yamdb_final
  

### Автор проекта: Кузнецов Антон
  

#### Технологии в проекте:
1. Python
2. Docker
  

### Описание проекта:
Настроить для приложения api_yamdb Continuous Integration и Continuous Deployment.  
Нужно реализовать:  
- автоматический запуск тестов,  
- обновление образов на Docker Hub,  
- автоматический деплой на боевой сервер при пуше в главную ветку main.  
  

### Запуск проекта
1. Клонировать проект с репозитория
2. Установить виртуальное окружение (python -m venv venv)
3. Активировать виртуальное окружение (. venv/scripts/activate)
3. Перейти в папку */api_yamdb* и установить зависимости (pip install -r requirements.txt)
  
  
### Описание команды для заполнения базы данными на сервере.
1. *sudo docker-compose exec web python manage.py migrate* - миграции
2. *sudo docker-compose exec web python manage.py createsuperuser* - создание суперюзера
3. *sudo docker-compose exec web python manage.py collectstatic --no-input* - собрать статику
4. *sudo docker-compose exec web python manage.py loaddata fixtures.json* - рименяются фикстуры


### Работающий проект:
http://158.160.42.132/admin/
  

### Ссылка на проект на GitHub:
https://github.com/anton1202-py/yamdb_final
  

### Примеры эндпоинтов проекта:
AUTH
POST http://158.160.42.132/api/v1/auth/signup/ - Регистрация нового пользователя

POST http://158.160.42.132/api/v1/auth/token/ - Получение JWT-токена

CATEGORIES
GET http://158.160.42.132/api/v1/categories/ - Получение списка всех категорий

POST http://158.160.42.132/api/v1/categories/ - Добавление новой категории

DEL http://158.160.42.132/api/v1/categories/{slug}/ - Удаление категории

GENRES
GET http://158.160.42.132/api/v1/genres/ - Получение списка всех жанров

POST http://158.160.42.132/api/v1/genres/ - Добавление жанра

DEL http://158.160.42.132/api/v1/genres/{slug}/ - Удаление жанра

TITLES
GET http://158.160.42.132/api/v1/titles/ - Получение списка всех произведений

POST http://158.160.42.132/api/v1/titles/ - Добавление произведения

GET http://158.160.42.132/api/v1/titles/{titles_id}/ - Получение информации о произведении

PATCH http://158.160.42.132/api/v1/titles/{titles_id}/ - Частичное обновление информации о произведении

DEL http://158.160.42.132/api/v1/titles/{titles_id}/ - Удаление произведения

REVIEWS
GET http://158.160.42.132/api/v1/titles/{title_id}/reviews/ - Получение списка всех отзывов

POST http://158.160.42.132/api/v1/titles/{title_id}/reviews/ - Добавление нового отзыва

GET http://158.160.42.132/api/v1/titles/{title_id}/reviews/{review_id}/ - Получение отзыва по id

PATCH http://158.160.42.132/api/v1/titles/{title_id}/reviews/{review_id}/ - Частичное обновление отзыва по id

DEL http://158.160.42.132/api/v1/titles/{title_id}/reviews/{review_id}/ - Удаление отзыва по id

COMMENTS
GET http://158.160.42.132/api/v1/titles/{title_id}/reviews/{review_id}/comments/ - Получение списка всех комментариев к отзыву

POST http://158.160.42.132/api/v1/titles/{title_id}/reviews/{review_id}/comments/ - Добавление комментария к отзыву

GET http://158.160.42.132/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/ - Получение комментария к отзыву

PATCH http://158.160.42.132/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/ - Частичное обновление комментария к отзыву

DEL http://158.160.42.132/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/ - Удаление комментария к отзыву

USERS
GET http://158.160.42.132/api/v1/users/ - Получение списка всех пользователей

POST http://158.160.42.132/api/v1/users/ - Добавление пользователя

GET http://158.160.42.132/api/v1/users/{username}/ - Получение пользователя по username
