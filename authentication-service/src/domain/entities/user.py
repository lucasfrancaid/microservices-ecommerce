from datetime import datetime
from dataclasses import dataclass
from random import randint
from typing import Optional, Union
from uuid import UUID


@dataclass
class UserEntity:
    user_id: Union[UUID, int, str, None]
    first_name: str
    last_name: str
    email: str
    hash_password: str
    is_active: Optional[bool] = False
    confirmation_code: Optional[int] = None
    created_at: Optional[datetime] = None

    def __post_init__(self):
        if not self.user_id and not self.is_active and not self.confirmation_code:
            self.confirmation_code = self.__factory_confirmation_code()
        if not self.created_at:
            self.created_at = datetime.now()

    @staticmethod
    def __factory_confirmation_code() -> int:
        code_digits = 6
        initial_range = 10**(code_digits - 1)
        final_range = 10**code_digits
        confirmation_code = randint(initial_range, final_range)
        return confirmation_code
