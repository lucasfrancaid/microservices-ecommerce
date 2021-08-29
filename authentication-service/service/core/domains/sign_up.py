from pydantic import BaseModel, validator


class SignUpDomain(BaseModel):
    full_name: str
    email: str
    password: str
    confirm_password: str

    @validator('full_name')
    def is_valid_full_name(cls, v):
        if len(v.split(' ')) <= 1:
            raise ValueError('Full name must be two words or more')
        return v

    @validator('password')
    def is_valid_password(cls, v):
        if len(v) < 8:
            raise ValueError('Length of password must be 8 or more')
        return v

    @validator('confirm_password')
    def password_match(cls, v, values, **kwargs):
        if values['password'] != v:
            raise ValueError('Password and Confirm Password must be equal')
        return v
