from pydantic import BaseModel, EmailStr, constr, validator


class SignUpEmailEntity(BaseModel):
    email: EmailStr


class SignUpEntity(SignUpEmailEntity):
    full_name: str
    password: constr(min_length=8)
    password_confirmation: constr(min_length=8)

    @validator('full_name')
    def is_valid_full_name(cls, v):
        if len(v.split(' ')) <= 1:
            raise ValueError('Full name must be two words or more')
        return v

    @validator('password_confirmation')
    def passwords_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('Password and Password Confirmation must be equal')
        return v


class SignUpConfirmationAccountEntity(SignUpEmailEntity):
    confirmation_code: int
