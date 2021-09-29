from ast import literal_eval
from typing import Dict

import pytest
from pydantic import ValidationError

from service.core.entities.user import UserEntity


def test_user_entity_from_dict(user_entity_dict: Dict):
    user_entity = UserEntity(**user_entity_dict)

    assert user_entity.user_id is None
    assert user_entity.first_name == user_entity_dict['first_name']
    assert user_entity.last_name == user_entity_dict['last_name']
    assert user_entity.email == user_entity_dict['email']
    assert user_entity.hash_password == user_entity_dict['hash_password']
    assert user_entity.is_active is False
    assert user_entity.confirmation_code is None


def test_user_entity_invalid_email_should_raise_validation_error(user_entity_dict: Dict):
    user_entity_dict['email'] = 'lucas.entity.com.br'

    with pytest.raises(ValidationError) as exc:
        UserEntity(**user_entity_dict)

    error = literal_eval(exc.value.json())[0]

    assert error['loc'][0] == 'email'
    assert error['msg'] == 'value is not a valid email address'
    assert error['type'] == 'value_error.email'
