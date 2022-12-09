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
2. *docker-compose exec web python manage.py createsuperuser* - создание суперюзера
3. *docker-compose exec web python manage.py collectstatic --no-input*  - собрать статику