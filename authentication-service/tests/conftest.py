import asyncio
from typing import Dict

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.factories.app import ApplicationFactory, factory_application
from src.infrastructure.factories.orm import SqlAlchemyFactory


@pytest.fixture(scope='session')
def fastapi_client() -> TestClient:
    from src.adapters.http.fastapi.main import app
    client = TestClient(app)
    return client


@pytest.fixture
async def factory() -> ApplicationFactory:
    return await factory_application()


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='session')
async def manage_database():
    from src.infrastructure.orm.sqlalchemy.database import Base, engine
    conn = await engine.begin()
    await conn.run_sync(Base.metadata.drop_all)
    await conn.run_sync(Base.metadata.create_all)
    yield conn
    await conn.run_sync(Base.metadata.drop_all)
    await conn.close()


@pytest.fixture
async def sqlalchemy_session(manage_database) -> AsyncSession:
    session = await SqlAlchemyFactory.session()
    yield session
    await session.close()


@pytest.fixture
def user_entity_dict() -> Dict:
    user = {
        'user_id': 1,
        'first_name': 'Lucas',
        'last_name': 'França',
        'email': 'lucas@entity.com',
        'hash_password': 'MyPass123'.encode(),
    }
    return user


@pytest.fixture
def send_email_entity_dict() -> Dict:
    send_email = {
        'subject': 'Your new account',
        'email_from': 'root@application.com',
        'email_to': ['lucas@application.com'],
        'body': 'You need confirm your new account'
    }
    return send_email


@pytest.fixture
def email_service_configuration_entity_dict() -> Dict:
    configuration = {
        'host': '127.0.0.1',
        'port': 25,
        'username': 'root',
        'password': 'toor',
    }
    return configuration


@pytest.fixture
def sign_up_entity_dict() -> Dict:
    sign_up = {
        'full_name': 'Lucas França',
        'email': 'lucas@entity.com',
        'password': 'MyPass123',
        'password_confirmation': 'MyPass123',
    }
    return sign_up


@pytest.fixture
def sign_up_confirmation_account_entity_dict() -> Dict:
    sign_up_confirmation = {'email': 'lucas.account@entity.com', 'confirmation_code': 123}
    return sign_up_confirmation
