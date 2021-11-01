# Exchange rates API

* [How to start](#how-to-start)
* [Secrets](#secrets)
* [API Authentication](#auth-examples)
* [Request & Response Examples](#request--response-examples)

## How to start

    $ docker-compose up

## Secrets

For the convenience of launching the project, I added .env file with the database credentials and the ALPHAVANTAGE API key to the repository.

## API Authentication

   - To get access to /api/v1/quotes/ resources user must be authenticated on the server using the Bearer Token authentication type.  
   - Below, you can see an example of registering a new user and obtaining/refreshing a token.
   - Token lifetime by default is set for 1 hour and can be changed through the Django settings file.

    SIMPLE_JWT = {
        'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
        'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    }


### Examples

  - [POST /auth/register/](#register-new-user)
  - [POST /auth/login/](#get-user-token)
  - [POST /auth/login/refresh/](#refresh-user-token)
  
### POST /auth/register/

Request body:

    {
        "username": "username",
        "password": "strong_password!",
        "password2": "strong_password!",
        "email": "email@example.com",
        "first_name": "first_name",
        "last_name": "last_name"
    }


Response body:

    {
        "username": "username",
        "email": "email@example.com",
        "first_name": "first_name",
        "last_name": "last_name"
    }

### POST /auth/login/

Request body:

    {
        "username": "username",
        "password": "strong_password!"
    }


Response body:

    {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzNTg4MjY2OCwiaWF0IjoxNjM1Nzk2MjY4LCJqdGkiOiI5MWZjYTk1Njg3ZTM0NTJiODBhNjA1OTkzYTAyNmFhYiIsInVzZXJfaWQiOjEsInVzZXJuYW1lIjoidGltX3l1bSJ9.UxV7hSCvsoZayQ8gYzyS1tqHvfYKzcU7_edtl47wVqo",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM1Nzk5ODY4LCJpYXQiOjE2MzU3OTYyNjgsImp0aSI6Ijg1YmVjMGIwZTE2MDQwM2ZiMmI3ZGQ5MTBiN2I3NWVmIiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJ0aW1feXVtIn0.wSQCKX2Dqhl8ggAJFKgrC0bYAYgb-_wRFGZVQ9x8EzQ"
    }

### POST /auth/login/refresh/

Request body:

    {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzNTg4MjY2OCwiaWF0IjoxNjM1Nzk2MjY4LCJqdGkiOiI5MWZjYTk1Njg3ZTM0NTJiODBhNjA1OTkzYTAyNmFhYiIsInVzZXJfaWQiOjEsInVzZXJuYW1lIjoidGltX3l1bSJ9.UxV7hSCvsoZayQ8gYzyS1tqHvfYKzcU7_edtl47wVqo",
    }


Response body:

    {
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM1Nzk5ODY4LCJpYXQiOjE2MzU3OTYyNjgsImp0aSI6Ijg1YmVjMGIwZTE2MDQwM2ZiMmI3ZGQ5MTBiN2I3NWVmIiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJ0aW1feXVtIn0.wSQCKX2Dqhl8ggAJFKgrC0bYAYgb-_wRFGZVQ9x8EzQ"
    }


## Request & Response Examples

### API Resources

  - [GET /api/v1/quotes/](#get-quotes)
  - [POST /api/v1/quotes/](#post-quotes)

### GET /api/v1/quotes/

Response body:

    [
        {
            "id": 1,
            "from_currency": "BTC",
            "to_currency": "USD",
            "rate": 60600.0,
            "timestamp": "2021-11-01T18:40:01Z"
        },
        {
            "id": 2,
            "from_currency": "BTC",
            "to_currency": "RUB",
            "rate": 4318878.65535,
            "timestamp": "2021-11-01T19:35:53Z"
        },
        {
            "id": 3,
            "from_currency": "BTC",
            "to_currency": "EUR",
            "rate": 52674.205286,
            "timestamp": "2021-11-01T19:36:02Z"
        }
    ]

### POST /api/v1/quotes/

Request body:

    {
        "from_currency": "BTC",
        "to_currency": "USD",
    }


Response body:

    {
        "id": 1,
        "from_currency": "BTC",
        "to_currency": "USD",
        "rate": 60600.0,
        "timestamp": "2021-11-01T18:40:01Z"
    }
