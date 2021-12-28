from typing import Dict

from src.application.mappers.user_dto import UserEntityDTO
from src.domain.entities.user import UserEntity
from src.adapters.http.common.schemas.user import UserSchema, UserSchemaDTO


def test_user_schema(user_entity_dict: Dict):
    user_entity = UserEntity(**user_entity_dict)
    user_schema = UserSchema(**user_entity.__dict__)

    user_schema_dict = {**user_schema.__dict__}
    user_schema_dict.pop('__initialised__')

    assert user_schema_dict == user_entity.__dict__


def test_user_schema_dto(user_entity_dict: Dict):
    user_entity_dto = UserEntityDTO(**user_entity_dict)

    user_schema = UserSchemaDTO(**user_entity_dto.__dict__)

    assert user_schema.__dict__ == user_entity_dto.__dict__


def test_user_schema_dto_from_user_entity(user_entity_dict: Dict):
    user_entity = UserEntity(**user_entity_dict)

    user_schema = UserSchemaDTO(**user_entity.__dict__)
    user_schema_dict = {**user_schema.__dict__}

    assert user_schema_dict['user_id'] == user_entity.user_id
    assert user_schema_dict['first_name'] == user_entity.first_name
    assert user_schema_dict['last_name'] == user_entity.last_name
    assert user_schema_dict['email'] == user_entity.email
    assert user_schema_dict.get('hash_password') is None
    assert user_schema_dict.get('is_active') is None
    assert user_schema_dict.get('confirmation_code') is None
    assert user_schema_dict.get('created_at') is None
