from typing import Dict

from service.core.entities.email import EmailConfigurationEntity, SendEmailEntity


def test_email_configuration_entity(email_configuration_entity_dict: Dict):
    configuration_entity = EmailConfigurationEntity(**email_configuration_entity_dict)

    assert configuration_entity.host == email_configuration_entity_dict['host']
    assert configuration_entity.port == email_configuration_entity_dict['port']
    assert configuration_entity.username == email_configuration_entity_dict['username']
    assert configuration_entity.password == email_configuration_entity_dict['password']
    assert configuration_entity.timeout == 60
    assert configuration_entity.use_tls is False
    assert configuration_entity.use_ssl is False
    assert configuration_entity.ssl_certfile is None


def test_send_email_entity(send_email_entity_dict: Dict):
    configuration_entity = SendEmailEntity(**send_email_entity_dict)

    assert configuration_entity.dict() == send_email_entity_dict
