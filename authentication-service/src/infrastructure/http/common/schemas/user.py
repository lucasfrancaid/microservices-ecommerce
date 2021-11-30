from pydantic.dataclasses import dataclass

from src.application.mappers.user_dto import UserEntityDTO
from src.domain.entities.user import UserEntity

UserSchema = dataclass(UserEntity)
UserSchemaDTO = dataclass(UserEntityDTO, init=False)
