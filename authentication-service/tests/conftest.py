from typing import Dict

import pytest

from src.infrastructure.factories.app import ApplicationFactory, factory_application


@pytest.fixture(scope='session')
def factory() -> ApplicationFactory:
    return factory_application()


@pytest.fixture
def user_entity_dict() -> Dict:
    user = {
        'user_id': 1,
        'first_name': 'Lucas',
        'last_name': 'França',
        'email': 'lucas@entity.com',
        'hash_password': 'MyPass123'.encode(),
    }
    return user


@pytest.fixture
def send_email_entity_dict() -> Dict:
    send_email = {
        'subject': 'Your new account',
        'email_from': 'root@application.com',
        'email_to': ['lucas@application.com'],
        'body': 'You need confirm your new account'
    }
    return send_email


@pytest.fixture
def email_service_configuration_entity_dict() -> Dict:
    configuration = {
        'host': '127.0.0.1',
        'port': 25,
        'username': 'root',
        'password': 'toor',
    }
    return configuration


@pytest.fixture
def sign_up_entity_dict() -> Dict:
    sign_up = {
        'full_name': 'Lucas França',
        'email': 'lucas@entity.com',
        'password': 'MyPass123',
        'password_confirmation': 'MyPass123',
    }
    return sign_up


@pytest.fixture
def sign_up_confirmation_account_entity_dict() -> Dict:
    sign_up_confirmation = {'email': 'lucas.account@entity.com', 'confirmation_code': 123}
    return sign_up_confirmation
