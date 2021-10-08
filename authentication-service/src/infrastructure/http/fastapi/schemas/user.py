from pydantic.dataclasses import dataclass

from src.core.domain.entities.user import UserEntity

UserSchema = dataclass(UserEntity)