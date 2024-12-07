from decouple import config
import os

SECRET_KEY = config('SECRET_KEY')
print(config("SQL_ENGINE"))

DATABASES = {
    'default': {
        'ENGINE': config("SQL_ENGINE"),
        'NAME': config("SQL_DATABASE"),
        'USER': config("SQL_USER"),
        'PASSWORD': config("SQL_PASSWORD"),
        'HOST': config("SQL_HOST"),
        'PORT': config("SQL_PORT"),
    }
}