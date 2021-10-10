import re
from typing import Dict, List, Optional, Union
from dataclasses import dataclass

from src.application.entities.exceptions import EmailEntityValidationError, SendEmailEntityValidationError


@dataclass
class EmailEntity:
    email: str

    def __post_init__(self):
        self.validate_email(self.email)

    @staticmethod
    def validate_email(email: str, exception_class: ValueError = EmailEntityValidationError) -> str:
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(email_pattern, email):
            raise exception_class(f'Email {email} is an invalid email')
        return email


@dataclass
class SendEmailEntity:
    subject: str
    email_from: str
    email_to: List[str]
    body: Union[Dict, str]

    def __post_init__(self):
        EmailEntity.validate_email(self.email_from, exception_class=SendEmailEntityValidationError)
        [EmailEntity.validate_email(email, exception_class=SendEmailEntityValidationError) for email in self.email_to]


@dataclass
class EmailServiceConfigurationEntity:
    host: str
    port: int
    username: str
    password: str
    timeout: Optional[int] = 60
    use_tls: Optional[bool] = False
    use_ssl: Optional[bool] = False
    ssl_certfile: Optional[str] = None
