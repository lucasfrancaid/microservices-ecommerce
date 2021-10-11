from pydantic.dataclasses import dataclass

from src.domain.entities.user import UserEntity

UserSchema = dataclass(UserEntity)
