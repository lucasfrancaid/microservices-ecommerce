from typing import Optional

from pydantic import BaseModel, EmailStr


class UserEntity(BaseModel):
    user_id: Optional[int] = None
    first_name: str
    last_name: str
    email: EmailStr
    hash_password: bytes
    is_active: Optional[bool] = False
    confirmation_code: Optional[int] = None
