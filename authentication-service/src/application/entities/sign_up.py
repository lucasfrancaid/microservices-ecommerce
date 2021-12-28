from dataclasses import dataclass

from src.application.entities.email import EmailEntity
from src.application.entities.exceptions import SignUpEntityValidationError, \
    SignUpConfirmationAccountEntityValidationError


@dataclass
class SignUpEntity:
    email: str
    full_name: str
    password: str
    password_confirmation: str

    def __post_init__(self):
        EmailEntity.validate_email(self.email, exception_class=SignUpEntityValidationError)
        self.validate_full_name(self.full_name)
        self.validate_password(self.password, self.password_confirmation)

    @staticmethod
    def validate_full_name(name: str) -> str:
        if len(name.split(' ')) <= 1:
            raise SignUpEntityValidationError('Full name must be two words or more')
        return name

    @staticmethod
    def validate_password(password: str, password_confirmation: str) -> str:
        if len(password) < 8:
            raise SignUpEntityValidationError('Password must be greater than or equal to 8 characters')
        if password != password_confirmation:
            raise SignUpEntityValidationError('Password and Password Confirmation must be equal')
        return password


@dataclass
class SignUpConfirmationAccountEntity:
    email: str
    confirmation_code: int

    def __post_init__(self):
        EmailEntity.validate_email(self.email, exception_class=SignUpConfirmationAccountEntityValidationError)
