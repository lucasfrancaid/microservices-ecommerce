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
