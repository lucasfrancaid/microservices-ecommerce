from typing import List

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from src.application.entities.sign_up import SignUpEntity, SignUpConfirmationAccountEntity
from src.application.ports.controllers.sign_up import SignUpController
from src.application.usecases.exceptions import SignUpConfirmationAccountUseCaseException
from src.infrastructure.factories.app import ApplicationFactory, factory_application
from src.infrastructure.http.common.schemas.user import UserSchema, UserSchemaDTO

controller = SignUpController()
sign_up_router = APIRouter(prefix='/sign-up', tags=['Sign Up'])


@sign_up_router.get('/users', response_model=List[UserSchema])
async def get_all_users(page: int = 1, limit: int = 20, factory: ApplicationFactory = Depends(factory_application)):
    response = [UserSchema(**user.__dict__) for user in await factory.repository.all(page=page, limit=limit)]
    return response


@sign_up_router.get('/user', response_model=UserSchema)
async def get_user(user_id: int = None, email: str = None, factory: ApplicationFactory = Depends(factory_application)):
    if not user_id and not email:
        return JSONResponse({'message': 'User id or email is required'}, HTTP_400_BAD_REQUEST)
    response = await factory.repository.get(user_id=user_id, email=email)
    if not response:
        return JSONResponse({'message': 'User not found'}, HTTP_404_NOT_FOUND)
    return UserSchemaDTO(**response.__dict__)


@sign_up_router.post('/register', response_model=UserSchema)
async def register_user(entity: SignUpEntity, factory: ApplicationFactory = Depends(factory_application)):
    response = await controller.post(
        repository=factory.repository,
        password_manager=factory.password_manager,
        email_service=factory.email_service,
        entity=entity
    )
    return UserSchema(**response)


@sign_up_router.put('/confirmation-account', response_model=UserSchema)
async def confirmation_account(entity: SignUpConfirmationAccountEntity,
                               factory: ApplicationFactory = Depends(factory_application)):
    try:
        response = await controller.put(repository=factory.repository, email_service=factory.email_service,
                                        entity=entity)
    except SignUpConfirmationAccountUseCaseException as exc:
        if str(exc) == 'User not found':
            return JSONResponse({'message': 'User not found'}, HTTP_404_NOT_FOUND)
    return UserSchema(**response)


@sign_up_router.delete('/{user_id}')
async def delete_user(user_id: int, factory: ApplicationFactory = Depends(factory_application)):
    deleted = await factory.repository.delete(user_id=user_id)
    if not deleted:
        return JSONResponse({'message': 'User was not deleted'}, HTTP_400_BAD_REQUEST)
    return JSONResponse({'message': 'User was deleted'}, HTTP_200_OK)
