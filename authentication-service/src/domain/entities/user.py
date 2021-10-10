from uuid import UUID
from typing import Optional, Union
from datetime import datetime
from dataclasses import dataclass


@dataclass
class UserEntity:
    user_id: Union[UUID, int, str, None]
    first_name: str
    last_name: str
    email: str
    hash_password: bytes
    is_active: Optional[bool] = False
    confirmation_code: Optional[int] = None
    created_at: Optional[datetime] = None

    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now()
