from typing import Dict

import pytest
from fastapi.testclient import TestClient

from src.domain.entities.user import UserEntity
from src.infrastructure.factories.app import ApplicationFactory

pytest.mock_user = {
    'user_id': None,
    'first_name': 'Lucas',
    'last_name': 'França',
    'email': 'lucas@client.com',
    'hash_password': 'MyPass123'.encode(),
}


@pytest.mark.fastapi
@pytest.mark.asyncio
async def test_get_all_users(fastapi_client: TestClient):
    response = fastapi_client.get('/sign-up/users')

    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.fastapi
@pytest.mark.asyncio
async def test_get_user(fastapi_client: TestClient, factory: ApplicationFactory):
    user = UserEntity(**pytest.mock_user)
    await factory.repository.create(user_entity=user)

    response = fastapi_client.get(f'/sign-up/user?email={user.email}')
    data = response.json()

    assert response.status_code == 200
    assert data['user_id'] is not None
    assert data['first_name'] == user.first_name
    assert data['last_name'] == user.last_name
    assert data['email'] == user.email

    await factory.repository.delete(user_id=user.user_id)


@pytest.mark.fastapi
@pytest.mark.asyncio
async def test_get_user_without_user_id_and_email_bad_request(fastapi_client: TestClient):
    response = fastapi_client.get(f'/sign-up/user')

    assert response.status_code == 400
    assert response.json() == {'message': 'User id or email is required'}


@pytest.mark.fastapi
@pytest.mark.asyncio
async def test_get_user_not_found(fastapi_client: TestClient):
    response = fastapi_client.get(f'/sign-up/user?user_id=12345')

    assert response.status_code == 404
    assert response.json() == {'message': 'User not found'}


@pytest.mark.fastapi
@pytest.mark.asyncio
async def test_register_user(fastapi_client: TestClient, sign_up_entity_dict: Dict, factory: ApplicationFactory):
    sign_up_entity_dict['email'] = pytest.mock_user['email']

    response = fastapi_client.post('/sign-up/register', json=sign_up_entity_dict)
    data = response.json()

    assert response.status_code == 200
    assert data['user_id'] is not None
    assert f'{data["first_name"]} {data["last_name"]}' == sign_up_entity_dict['full_name']
    assert data['email'] == sign_up_entity_dict['email']
    assert data['hash_password'] is not None
    assert data['is_active'] is False
    assert data['confirmation_code'] is not None
    assert data['created_at'] is not None

    registered_user = await factory.repository.get(email=sign_up_entity_dict['email'])
    assert registered_user is not None
    pytest.mock_user = {**registered_user.__dict__}


@pytest.mark.fastapi
@pytest.mark.asyncio
async def test_confirmation_account(fastapi_client: TestClient):
    payload = {'email': pytest.mock_user['email'], 'confirmation_code': pytest.mock_user['confirmation_code']}

    response = fastapi_client.put('/sign-up/confirmation-account', json=payload)
    data = response.json()

    assert response.status_code == 200
    assert data['user_id'] == pytest.mock_user['user_id']
    assert data['is_active'] is True


@pytest.mark.fastapi
@pytest.mark.asyncio
async def test_confirmation_account_not_found(fastapi_client: TestClient):
    payload = {'email': 'lucas.non-exists@client.com', 'confirmation_code': 2134}

    response = fastapi_client.put('/sign-up/confirmation-account', json=payload)

    assert response.status_code == 404
    assert response.json() == {'message': 'User not found'}


@pytest.mark.fastapi
@pytest.mark.asyncio
async def test_delete_user(fastapi_client: TestClient):
    response = fastapi_client.delete(f'/sign-up/{pytest.mock_user["user_id"]}')

    assert response.status_code == 200
    assert response.json() == {'message': 'User was deleted'}


@pytest.mark.fastapi
@pytest.mark.asyncio
async def test_delete_user_non_exists_bad_request(fastapi_client: TestClient):
    response = fastapi_client.delete(f'/sign-up/{23223333 * 1203232}')

    assert response.status_code == 400
    assert response.json() == {'message': 'User was not deleted'}
