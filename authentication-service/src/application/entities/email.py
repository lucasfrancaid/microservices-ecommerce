from typing import Dict, List, Optional, Union
from dataclasses import dataclass

from src.application.entities.exceptions import EmailEntityValidationError, SendEmailEntityValidationError
from src.application.validators.email import EmailValidator


@dataclass
class EmailEntity:
    email: str

    def __post_init__(self):
        EmailValidator.validate_email(self.email, exception_class=EmailEntityValidationError)


@dataclass
class SendEmailEntity:
    subject: str
    email_from: str
    email_to: List[str]
    body: Union[Dict, str]

    def __post_init__(self):
        EmailValidator.validate_email(self.email_from, exception_class=SendEmailEntityValidationError)
        [
            EmailValidator.validate_email(email, exception_class=SendEmailEntityValidationError)
            for email in self.email_to
        ]


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
