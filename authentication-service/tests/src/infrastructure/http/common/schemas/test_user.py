from typing import Dict

from src.domain.entities.user import UserEntity
from src.infrastructure.http.common.schemas.user import UserSchema


def test_user_schema(user_entity_dict: Dict):
    user_entity = UserEntity(**user_entity_dict)
    user_schema = UserSchema(**user_entity.__dict__)

    user_schema_dict = {**user_schema.__dict__}
    user_schema_dict.pop('__initialised__')

    assert user_schema_dict == user_entity.__dict__
