from typing import Dict

from src.application.mappers.user_dto import UserEntityDTO
from src.domain.entities.user import UserEntity


def test_user_dto(user_entity_dict: Dict):
    user_entity = UserEntity(**user_entity_dict)

    user_entity_dto = UserEntityDTO(**user_entity.__dict__)

    assert user_entity_dto.user_id == user_entity.user_id
    assert user_entity_dto.first_name == user_entity.first_name
    assert user_entity_dto.last_name == user_entity.last_name
    assert user_entity_dto.email == user_entity.email
    assert not getattr(user_entity_dto, 'hash_password', None)
    assert not getattr(user_entity_dto, 'is_active', None)
    assert not getattr(user_entity_dto, 'confirmation_code', None)
    assert not getattr(user_entity_dto, 'created_at', None)
