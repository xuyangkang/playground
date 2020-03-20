# Django

## Design Purposal
We'll use Django to build backend server. The reasons are:
- We need python to integrate with ML stack
- We don't want to build a user management system by ourself. Django has a good community support
- Authencitation is done by token, so that it could be used by both web and mobile.
- We won't use django's template, because it is difficult to use. We'll make Django a backend only server

## Install

```shell
pip install django
pip install djangorestframework
pip install markdown
pip install django-filter
```

## Usage
1. Create a super user, with username 'xuyang' and password 'password'
    ```shell
    python manage.py createsuperuser
    ```
2. Login to get auth token
    ```
    curl -H "Content-Type: application/json" -X POST --data '{"username":"xuyang","password":"password"}' http://127.0.0.1:8000/api-token-auth/
    ```
3. Run
    ```
    curl -H "Authorization: Token 45dbcacf94fda92e420012a405091f20453672b2" http://127.0.0.1:8000/secret/
    ```
    to access the API that requires authentication

## TODO
1. How to expire the token
2. How to safely build a login web UI
3. How to safely save the token in app
4. Setup django security: [https://docs.djangoproject.com/en/3.0/topics/security/](https://docs.djangoproject.com/en/3.0/topics/security/)
