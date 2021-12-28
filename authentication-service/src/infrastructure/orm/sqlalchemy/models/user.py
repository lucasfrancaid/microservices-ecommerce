from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String

from src.infrastructure.orm.sqlalchemy.database import Base


def datetime_now():
    return datetime.now()


class BaseModel(Base):
    __abstract__ = True

    created_at = Column(DateTime, default=datetime_now())
    updated_at = Column(DateTime, default=datetime_now(), onupdate=datetime_now())


class User(BaseModel):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    hash_password = Column(String)
    is_active = Column(Boolean, default=False)
    confirmation_code = Column(Integer, default=None)
