from typing import Dict

import pytest


@pytest.fixture
def email_configuration_entity_dict() -> Dict:
    email_configuration = {
        'host': '127.0.0.1',
        'port': 25,
        'username': 'root',
        'password': 'toor',
    }
    return email_configuration


@pytest.fixture
def send_email_entity_dict() -> Dict:
    send_email = {
        'subject': 'Send Email Test',
        'email_from': 'from@root.com',
        'email_to': ['to@root.com'],
        'body': 'A simple email text',
    }
    return send_email


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
    sign_up_confirmation = {
        'email': 'lucas@entity.com.br',
        'confirmation_code': 123
    }
    return sign_up_confirmation


@pytest.fixture
def user_entity_dict() -> Dict:
    user = {
        'first_name': 'Lucas',
        'last_name': 'França',
        'email': 'lucas@entity.com',
        'hash_password': 'MyPass123'.encode(),
    }
    return user
