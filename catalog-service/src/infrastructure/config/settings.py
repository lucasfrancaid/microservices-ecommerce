from decouple import config


class Settings:
    ENVIRONMENT = config('ENVIRONMENT', default='dev')
    DEBUG = config('DEBUG', default=False, cast=bool)
    APP_HOST = config('APP_HOST', default='0.0.0.0')
    APP_PORT = config('APP_POST', default=8001, cast=int)
    DATABASE_URL = config('DATABASE_URL')


static_settings = Settings()
