from abc import ABC, abstractmethod
from typing import Any

from src.application.entities.email import SendEmailEntity, EmailServiceConfigurationEntity


class EmailService(ABC):

    @abstractmethod
    def send(self, email_entity: SendEmailEntity = None):
        raise NotImplementedError


class EmailServiceFake(EmailService):

    def __init__(self, configuration: EmailServiceConfigurationEntity = None) -> None:
        self.configuration: EmailServiceConfigurationEntity = configuration

    def send(self, email_entity: SendEmailEntity = None) -> Any:
        pass
