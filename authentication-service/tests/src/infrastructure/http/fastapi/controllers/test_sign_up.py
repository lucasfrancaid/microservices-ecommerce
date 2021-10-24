from copy import deepcopy
from typing import Dict

import pytest
from fastapi.testclient import TestClient

from src.domain.entities.user import UserEntity
from src.infrastructure.factories.app import ApplicationFactory
from src.infrastructure.http.fastapi.main import app

client = TestClient(app)
pytest.mock_user = {
    'user_id': 2320323 * 1203232,
    'first_name': 'Lucas',
    'last_name': 'França',
    'email': 'lucas@client.com',
    'hash_password': 'MyPass123'.encode(),
}


def test_get_all_users():
    response = client.get('/sign-up/users')

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_user(factory: ApplicationFactory):
    user = UserEntity(**pytest.mock_user)
    factory.repository.create(user_entity=user)

    response = client.get(f'/sign-up/user?user_id={user.user_id}')
    data = response.json()

    assert response.status_code == 200
    assert data['user_id'] == user.user_id
    assert data['first_name'] == user.first_name
    assert data['last_name'] == user.last_name
    assert data['email'] == user.email
    assert data['hash_password'] == user.hash_password.decode()
    assert data['is_active'] == user.is_active
    assert data['confirmation_code'] == user.confirmation_code
    assert data['created_at'] == user.created_at.isoformat()

    factory.repository.delete(user_id=user.user_id)


def test_get_user_without_user_id_and_email_bad_request():
    response = client.get(f'/sign-up/user')

    assert response.status_code == 400
    assert response.json() == {'message': 'User id or email is required'}


def test_get_user_not_found():
    response = client.get(f'/sign-up/user?user_id=12345')

    assert response.status_code == 404
    assert response.json() == {'message': 'User not found'}


def test_register_user(sign_up_entity_dict: Dict, factory: ApplicationFactory):
    sign_up_entity_dict['email'] = pytest.mock_user['email']

    response = client.post('/sign-up/register', json=sign_up_entity_dict)
    data = response.json()

    assert response.status_code == 200
    assert data['user_id'] is not None
    assert f'{data["first_name"]} {data["last_name"]}' == sign_up_entity_dict['full_name']
    assert data['email'] == sign_up_entity_dict['email']
    assert data['hash_password'] is not None
    assert data['is_active'] is False
    assert data['confirmation_code'] is not None
    assert data['created_at'] is not None

    assert factory.repository.get(email=sign_up_entity_dict['email'])
    pytest.mock_user = deepcopy(data)


def test_confirmation_account():
    payload = {'email': pytest.mock_user['email'], 'confirmation_code': pytest.mock_user['confirmation_code']}

    response = client.put('/sign-up/confirmation-account', json=payload)
    data = response.json()

    assert response.status_code == 200
    assert data['user_id'] == pytest.mock_user['user_id']
    assert data['is_active'] is True


def test_confirmation_account_not_found():
    payload = {'email': 'lucas.non-exists@client.com', 'confirmation_code': 2134}

    response = client.put('/sign-up/confirmation-account', json=payload)

    assert response.status_code == 404
    assert response.json() == {'message': 'User not found'}


def test_delete_user():
    response = client.delete(f'/sign-up/{pytest.mock_user["user_id"]}')

    assert response.status_code == 200
    assert response.json() == {'message': 'User was deleted'}


def test_delete_user_non_exists_bad_request():
    response = client.delete(f'/sign-up/{23223333 * 1203232}')

    assert response.status_code == 400
    assert response.json() == {'message': 'User was not deleted'}
