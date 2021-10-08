from typing import Dict

import pytest

from src.application.entities.email import EmailEntity, SendEmailEntity, EmailServiceConfigurationEntity
from src.application.entities.exceptions import EmailEntityValidationError, SendEmailEntityValidationError


def test_email_entity():
    email = 'lucas@entity.com.br'
    email_entity = EmailEntity(email=email)

    assert email_entity.email == email


def test_email_entity_invalid_email_should_raise_validation_error():
    email = 'luc@s@entity.com.br'

    with pytest.raises(EmailEntityValidationError) as exc:
        EmailEntity(email=email)

    assert str(exc.value) == f'Email {email} is an invalid email'


def test_send_email_entity(send_email_entity_dict: Dict):
    send_email_entity = SendEmailEntity(**send_email_entity_dict)

    assert send_email_entity.__dict__ == send_email_entity_dict


def test_send_email_entity_invalid_email_from_should_raise_validation_error(send_email_entity_dict: Dict):
    invalid_email = 'luc@s!en#tity.com.br'
    send_email_entity_dict['email_from'] = invalid_email

    with pytest.raises(SendEmailEntityValidationError) as exc:
        SendEmailEntity(**send_email_entity_dict)

    assert str(exc.value) == f'Email {invalid_email} is an invalid email'


def test_send_email_entity_invalid_email_to_should_raise_validation_error(send_email_entity_dict: Dict):
    invalid_email = 'lucas.entity.com.br'
    send_email_entity_dict['email_to'] = [invalid_email]

    with pytest.raises(SendEmailEntityValidationError) as exc:
        SendEmailEntity(**send_email_entity_dict)

    assert str(exc.value) == f'Email {invalid_email} is an invalid email'


def test_email_service_configuration_entity(email_service_configuration_entity_dict: Dict):
    configuration_entity = EmailServiceConfigurationEntity(**email_service_configuration_entity_dict)

    assert configuration_entity.host == email_service_configuration_entity_dict['host']
    assert configuration_entity.port == email_service_configuration_entity_dict['port']
    assert configuration_entity.username == email_service_configuration_entity_dict['username']
    assert configuration_entity.password == email_service_configuration_entity_dict['password']
    assert configuration_entity.timeout == 60
    assert configuration_entity.use_tls is False
    assert configuration_entity.use_ssl is False
    assert configuration_entity.ssl_certfile is None
