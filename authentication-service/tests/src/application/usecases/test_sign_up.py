from datetime import datetime
from typing import Dict

import pytest

from src.domain.entities.user import UserEntity
from src.application.entities.email import EmailEntity
from src.application.entities.sign_up import SignUpEntity, SignUpConfirmationAccountEntity
from src.application.ports.repositories.authentication import AuthenticationRepositoryInMemory
from src.application.services.email import EmailServiceFake
from src.application.security.password_manager import PasswordManagerFake
from src.application.usecases.sign_up import SignUpConfirmationAccountUseCase, SignUpUseCase
from src.application.usecases.exceptions import SignUpUseCaseException, SignUpConfirmationAccountUseCaseException, \
    SignUpConfirmationAccountUseCaseValidationError

repository = AuthenticationRepositoryInMemory()
password_manager = PasswordManagerFake()
email_service = EmailServiceFake()


@pytest.mark.asyncio
async def test_sign_up_use_case_serialize(sign_up_entity_dict: Dict):
    sign_up_entity = SignUpEntity(**sign_up_entity_dict)
    use_case = SignUpUseCase(repository=repository, password_manager=password_manager, email_service=email_service)

    serialized_user = await use_case.serialize(entity=sign_up_entity)

    assert serialized_user.user_id is None
    assert f'{serialized_user.first_name} {serialized_user.last_name}' == sign_up_entity.full_name
    assert serialized_user.email == sign_up_entity.email
    assert serialized_user.hash_password == sign_up_entity.password.encode()
    assert serialized_user.is_active is False
    assert serialized_user.confirmation_code is None


@pytest.mark.asyncio
async def test_sign_up_use_case_deserialize(user_entity_dict: Dict):
    user_entity = UserEntity(**user_entity_dict)
    use_case = SignUpUseCase(repository=repository, password_manager=password_manager, email_service=email_service)

    deserialized_user = await use_case.deserialize(user_entity=user_entity)

    assert isinstance(deserialized_user, dict)
    assert deserialized_user == user_entity.__dict__


@pytest.mark.asyncio
async def test_sign_up_use_case_check_if_email_is_available():
    entity = EmailEntity(email='lucas@domain.com')
    use_case = SignUpUseCase(repository=repository, password_manager=password_manager, email_service=email_service)

    assert await use_case.check_if_email_is_available(email=entity.email) is True


@pytest.mark.asyncio
async def test_sign_up_use_case_user_register(user_entity_dict: Dict):
    user_entity = UserEntity(**user_entity_dict)
    use_case = SignUpUseCase(repository=repository, password_manager=password_manager, email_service=email_service)

    registered_user = await use_case.user_register(user_entity=user_entity)

    assert isinstance(registered_user.user_id, int)
    assert registered_user.email == user_entity.email
    assert isinstance(registered_user.hash_password, bytes)
    assert isinstance(registered_user.created_at, datetime)


@pytest.mark.asyncio
async def test_sign_up_use_case_send_email(user_entity_dict: Dict):
    user_entity = UserEntity(**user_entity_dict)
    use_case = SignUpUseCase(repository=repository, password_manager=password_manager, email_service=email_service)

    assert await use_case.send_email(user_entity=user_entity) is None


@pytest.mark.asyncio
async def test_sign_up_use_case_handler(sign_up_entity_dict: Dict):
    sign_up_entity = SignUpEntity(**sign_up_entity_dict)
    use_case = SignUpUseCase(repository=repository, password_manager=password_manager, email_service=email_service)

    registered_user = await use_case.handler(entity=sign_up_entity)

    assert registered_user['user_id'] is not None
    assert registered_user['email'] == sign_up_entity.email
    assert isinstance(registered_user['hash_password'], bytes)
    assert registered_user['hash_password'] == sign_up_entity.password.encode()
    assert f'{registered_user["first_name"]} {registered_user["last_name"]}' == sign_up_entity.full_name
    assert registered_user['is_active'] is False
    assert registered_user['confirmation_code'] is not None


@pytest.mark.asyncio
async def test_sign_up_use_case_handler_user_email_is_active_must_raise_exception(sign_up_entity_dict: Dict):
    sign_up_entity = SignUpEntity(**sign_up_entity_dict)
    user = await repository.get(email=sign_up_entity.email)
    user.is_active = True
    await repository.update(user_id=user.user_id, user_entity=user)

    use_case = SignUpUseCase(repository=repository, password_manager=password_manager, email_service=email_service)

    with pytest.raises(SignUpUseCaseException) as exc:
        await use_case.handler(entity=sign_up_entity)

    assert str(exc.value) == 'Email is not available'


@pytest.mark.asyncio
async def test_sign_up_confirmation_account_use_case_serialize_must_raise_not_implemented_error():
    use_case = SignUpConfirmationAccountUseCase(repository=repository, email_service=email_service)

    with pytest.raises(NotImplementedError):
        await use_case.serialize()


@pytest.mark.asyncio
async def test_sign_up_confirmation_account_use_case_deserialize(user_entity_dict: Dict):
    user_entity = UserEntity(**user_entity_dict)
    use_case = SignUpConfirmationAccountUseCase(repository=repository, email_service=email_service)

    deserialized_user = await use_case.deserialize(user_entity=user_entity)

    assert isinstance(deserialized_user, dict)
    assert deserialized_user == user_entity.__dict__


@pytest.mark.asyncio
async def test_sign_up_confirmation_account_use_case_handler(
    sign_up_confirmation_account_entity_dict: Dict, user_entity_dict: Dict
):
    entity = SignUpConfirmationAccountEntity(**sign_up_confirmation_account_entity_dict)
    user_entity = UserEntity(**user_entity_dict)
    use_case = SignUpConfirmationAccountUseCase(repository=repository, email_service=email_service)

    user_entity.user_id = 999
    user_entity.email = entity.email
    user_entity.is_active = False
    user_entity.confirmation_code = entity.confirmation_code
    repository.storage.data.append(user_entity)

    confirmed_user = await use_case.handler(confirmation_entity=entity)

    assert confirmed_user['is_active'] is True


@pytest.mark.asyncio
async def test_sign_up_confirmation_account_use_case_handler_non_existent_user_must_raise_exception(
    sign_up_confirmation_account_entity_dict: Dict
):
    use_case = SignUpConfirmationAccountUseCase(repository=repository, email_service=email_service)
    entity = SignUpConfirmationAccountEntity(**sign_up_confirmation_account_entity_dict)
    entity.email = 'non.existent@entity.com'

    with pytest.raises(SignUpConfirmationAccountUseCaseException) as exc:
        await use_case.handler(confirmation_entity=entity)

    assert str(exc.value) == 'User not found'


@pytest.mark.asyncio
async def test_sign_up_confirmation_account_use_case_handler_invalid_confirmation_code_must_raise_exception(
    sign_up_confirmation_account_entity_dict: Dict
):
    entity = SignUpConfirmationAccountEntity(**sign_up_confirmation_account_entity_dict)
    entity.confirmation_code = 456
    use_case = SignUpConfirmationAccountUseCase(repository=repository, email_service=email_service)

    with pytest.raises(SignUpConfirmationAccountUseCaseValidationError) as exc:
        await use_case.handler(confirmation_entity=entity)

    assert str(exc.value) == 'Incorrect confirmation code'
