from uuid import UUID
from typing import Union
from dataclasses import dataclass

from src.application.patterns.dto import DataclassDTO


@dataclass(init=False)
class UserEntityDTO(DataclassDTO):
    user_id: Union[UUID, int, str]
    first_name: str
    last_name: str
    email: str
