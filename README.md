# API для реферальной системы

Простой RESTful API сервис для реферальной системы.

## Как запустить проект

Скачать удаленный репозиторий выполнив команду

```
git clone https://github.com/AlekseiTolchin/referral_project.git
```

В корневой директории проекта создать файл `.env` со следующими настройками:

- `SECRET_KEY`=django
- `DEBUG`=True
- `POSTGRES_USER`=user
- `POSTGRES_PASSWORD`=user
- `POSTGRES_DB`=referrals
- `DATABASE_URL`=postgres://user:user@postgres:5432/referrals
- `DJANGO_SUPERUSER_EMAIL`=admin@example.com
- `DJANGO_SUPERUSER_USERNAME`=admin
- `DJANGO_SUPERUSER_PASSWORD`=admin
- `ALLOWED_HOSTS`=0.0.0.0
- `ROTATE_REFRESH_TOKENS`=True
- `BLACKLIST_AFTER_ROTATION`=True
- `ACCESS_TOKEN_LIFETIME`=7
- `REFRESH_TOKEN_LIFETIME`=30

Запустить команды:

```
docker-compose build
```

```
docker-compose up
```

Ссылки для тестирования:

http://0.0.0.0:8000/api/docs/ - `документация API`  
http://0.0.0.0:8000/admin/ - `админ-панель`
