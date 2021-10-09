from typing import List

import bcrypt
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from src.main import FactoryApplication
from src.application.entities.sign_up import SignUpEntity, SignUpConfirmationAccountEntity
from src.application.ports.controllers.sign_up import SignUpController
from src.application.ports.repositories.authentication import AuthenticationRepositoryInMemory
from src.application.services.email import EmailServiceFake
from src.infrastructure.security.bcrypt import PasswordManagerBcrypt
from src.infrastructure.http.fastapi.schemas.user import UserSchema

controller = SignUpController()
factory = FactoryApplication(
    repository=AuthenticationRepositoryInMemory(),
    password_manager=PasswordManagerBcrypt(salt=bcrypt.gensalt()),
    email_service=EmailServiceFake()
)
sign_up_router = APIRouter(prefix='/sign-up', tags=['Sign Up'])


@sign_up_router.get('/users', response_model=List[UserSchema])
def get_all_users(page: int = 1, limit: int = 20):
    response = [UserSchema(**user.__dict__) for user in factory.repository.all(page=page, limit=limit)]
    return response


@sign_up_router.get('/user', response_model=UserSchema)
def get_user(user_id: int = None, email: str = None):
    if not user_id and not email:
        return JSONResponse({'message': 'User id or email is required'}, HTTP_400_BAD_REQUEST)
    response = factory.repository.get(user_id=user_id, email=email)
    return UserSchema(**response.__dict__)


@sign_up_router.post('/', response_model=UserSchema)
def sign_up(entity: SignUpEntity):
    response = controller.post(
        repository=factory.repository,
        password_manager=factory.password_manager,
        email_service=factory.email_service,
        entity=entity
    )
    return UserSchema(**response.__dict__)


@sign_up_router.put('/confirmation-account', response_model=UserSchema)
def confirmation_account(entity: SignUpConfirmationAccountEntity):
    response = controller.put(
        repository=factory.repository,
        email_service=factory.email_service,
        entity=entity
    )
    return UserSchema(**response.__dict__)


@sign_up_router.delete('/delete/{user_id}')
def delete_user(user_id: int):
    deleted = factory.repository.delete(user_id=user_id)
    if not deleted:
        return JSONResponse({'message': 'User was not deleted'}, HTTP_400_BAD_REQUEST)
    return JSONResponse({'message': 'User was deleted'}, HTTP_200_OK)
