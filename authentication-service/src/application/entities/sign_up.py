from dataclasses import dataclass

from src.application.entities.exceptions import SignUpEntityValidationError, \
    SignUpConfirmationAccountEntityValidationError
from src.application.validators.email import EmailValidator
from src.application.validators.password import PasswordValidator


@dataclass
class SignUpEntity:
    email: str
    full_name: str
    password: str
    password_confirmation: str

    def __post_init__(self):
        EmailValidator.validate_email(self.email, exception_class=SignUpEntityValidationError)
        self.validate_full_name(self.full_name)
        PasswordValidator.validate_password_rules(self.password, exception_class=SignUpEntityValidationError)
        PasswordValidator.validate_password_confirmation(
            self.password, self.password_confirmation, exception_class=SignUpEntityValidationError
        )

    @staticmethod
    def validate_full_name(name: str) -> str:
        if len(name.split(' ')) <= 1:
            raise SignUpEntityValidationError('Full name must be two words or more')
        return name


@dataclass
class SignUpConfirmationAccountEntity:
    email: str
    confirmation_code: int

    def __post_init__(self):
        EmailValidator.validate_email(self.email, exception_class=SignUpConfirmationAccountEntityValidationError)
