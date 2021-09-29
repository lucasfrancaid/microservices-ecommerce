from typing import Dict

import pytest


@pytest.fixture
def sign_up_entity_dict() -> Dict:
    sign_up = {
        'full_name': 'Lucas França',
        'email': 'lucas@domain.com',
        'password': 'MyPass123',
        'password_confirmation': 'MyPass123',
    }
    return sign_up


@pytest.fixture
def user_entity_dict() -> Dict:
    user = {
        'first_name': 'Lucas',
        'last_name': 'França',
        'email': 'lucas@domain.com',
        'hash_password': 'MyPass123'.encode(),
    }
    return user
