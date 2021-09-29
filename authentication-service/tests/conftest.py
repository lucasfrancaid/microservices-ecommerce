from typing import Dict

import pytest


@pytest.fixture
def sign_up_dict() -> Dict:
    sign_up = {
        'full_name': 'Lucas França',
        'email': 'lucas@domain.com',
        'password': 'MyPass123',
        'password_confirmation': 'MyPass123',
    }
    return sign_up
