from decouple import config


class Settings:
    DEBUG = config('DEBUG', default=False, cast=bool)
    APP_HOST = config('APP_HOST', default='127.0.0.1')
    APP_PORT = config('APP_POST', default=8000, cast=int)
    PASSWORD_SALT = config('PASSWORD_SALT').encode()
    DATABASE_STRATEGY = config('DATABASE_STRATEGY', default='memory')
    DATABASE_URL = config('DATABASE_URL', default='sqlite:///./authentication.db')
    EMAIL = {
        'HOST': config('EMAIL_HOST'),
        'PORT': config('EMAIL_PORT', default=255, cast=int),
        'USER': config('EMAIL_USER'),
        'PASSWORD': config('EMAIL_PASSWORD'),
        'USE_TLS': config('EMAIL_USE_TLS', default=False, cast=bool),
    }


static_settings = Settings()
