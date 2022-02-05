import re

from src.application.validators.exceptions import EmailValidatorError


class EmailValidator:

    @staticmethod
    def validate_email(email: str, exception_class: ValueError = EmailValidatorError) -> str:
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(email_pattern, email):
            raise exception_class(f'Email {email} is an invalid email')
        return email
