from typing import Dict
from datetime import datetime
from zoneinfo import ZoneInfo

from src.domain.entities.user import UserEntity


def test_user_entity(user_entity_dict: Dict):
    user_entity = UserEntity(**user_entity_dict)

    assert user_entity.user_id == 1
    assert user_entity.first_name == user_entity_dict['first_name']
    assert user_entity.last_name == user_entity_dict['last_name']
    assert user_entity.email == user_entity_dict['email']
    assert user_entity.hash_password == user_entity_dict['hash_password']
    assert user_entity.is_active is False
    assert user_entity.confirmation_code is None
    assert user_entity.created_at is not None


def test_user_entity_created_at_self_datetime(user_entity_dict: Dict):
    user_entity_dict['created_at'] = None
    user_entity = UserEntity(**user_entity_dict)

    assert user_entity_dict['created_at'] is None
    assert isinstance(user_entity.created_at, datetime)


def test_user_entity_created_at_custom_datetime(user_entity_dict: Dict):
    datetime_now = datetime.now(ZoneInfo('America/Sao_Paulo'))
    user_entity_dict['created_at'] = datetime_now
    user_entity = UserEntity(**user_entity_dict)

    assert user_entity.created_at == datetime_now


def test_user_entity_factory_confirmation_code(user_entity_dict: Dict):
    user_entity_dict['user_id'] = None
    assert user_entity_dict.get('confirmation_code') is None

    user_entity = UserEntity(**user_entity_dict)

    assert isinstance(user_entity.confirmation_code, int)
    assert len(str(user_entity.confirmation_code)) == 6


def test_user_entity_factory_confirmation_code_should_not_be_called_when_user_id_or_is_active_is_true(
    user_entity_dict: Dict
):
    user_entity_dict['is_active'] = True
    assert user_entity_dict.get('confirmation_code') is None

    user_entity = UserEntity(**user_entity_dict)

    assert user_entity.confirmation_code is None
