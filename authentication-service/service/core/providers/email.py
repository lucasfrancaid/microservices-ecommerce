from abc import ABC, abstractmethod
from typing import Any

from service.core.entities.email import EmailConfigurationEntity, SendEmailEntity


class EmailProvider(ABC):

    @abstractmethod
    def __init__(configuration: EmailConfigurationEntity):
        raise NotImplementedError

    @abstractmethod
    def send(email_entity: SendEmailEntity) -> Any:
        raise NotImplementedError


class EmailProviderNone(EmailProvider):

    def __init__(self, configuration: EmailConfigurationEntity = None):
        self.configuration: EmailConfigurationEntity = configuration
    
    def send(self, email_entity: SendEmailEntity = None) -> Any:
        pass
