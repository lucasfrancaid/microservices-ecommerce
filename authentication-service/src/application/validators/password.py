from src.application.validators.exceptions import PasswordValidatorError


class PasswordValidator:

    @staticmethod
    def validate_password_rules(password: str, exception_class: ValueError = PasswordValidatorError) -> str:
        if len(password) < 8:
            raise exception_class('Password must be greater than or equal to 8 characters')
        return password

    @staticmethod
    def validate_password_confirmation(
        password: str, password_confirmation: str, exception_class: ValueError = PasswordValidatorError
    ) -> str:
        if password != password_confirmation:
            raise exception_class('Password and Password Confirmation must be equal')
        return password
