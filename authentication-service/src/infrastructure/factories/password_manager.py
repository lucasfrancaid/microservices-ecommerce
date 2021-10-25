from src.infrastructure.config.settings import static_settings
from src.infrastructure.security.bcrypt import PasswordManagerBcrypt


class PasswordManagerFactory:

    @staticmethod
    def bcrypt() -> PasswordManagerBcrypt:
        return PasswordManagerBcrypt(salt=static_settings.PASSWORD_SALT)
