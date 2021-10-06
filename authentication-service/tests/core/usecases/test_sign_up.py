from typing import Dict

import pytest

from service.core.entities.user import UserEntity
from service.core.entities.sign_up import SignUpEmailEntity, SignUpEntity, SignUpConfirmationAccountEntity
from service.core.providers.email import EmailProviderNone
from service.core.repositories.authentication import AuthenticationRepositoryInMemory
from service.core.security.password_manager import PasswordManagerNone
from service.core.usecases.sign_up import SignUpConfirmationAccountUseCase, SignUpUseCase

repository = AuthenticationRepositoryInMemory()
password_manager = PasswordManagerNone()
email_provider = EmailProviderNone()


def test_sign_up_use_case_serialize(sign_up_entity_dict: Dict):
    sign_up_entity = SignUpEntity(**sign_up_entity_dict)
    use_case = SignUpUseCase(
        repository=repository,
        password_manager=password_manager,
        email_provider=email_provider
    )

    serialized_user: UserEntity = use_case.serialize(entity=sign_up_entity)

    assert serialized_user.user_id is None
    assert f'{serialized_user.first_name} {serialized_user.last_name}' == sign_up_entity.full_name
    assert serialized_user.email == sign_up_entity.email
    assert serialized_user.hash_password == sign_up_entity.password.encode()
    assert serialized_user.is_active is False
    assert serialized_user.confirmation_code is None


def test_sign_up_use_case_deserialize(user_entity_dict: Dict):
    user_entity = UserEntity(**user_entity_dict)
    use_case = SignUpUseCase(
        repository=repository,
        password_manager=password_manager,
        email_provider=email_provider
    )

    deserialized_user = use_case.deserialize(user_entity=user_entity)

    assert isinstance(deserialized_user, dict)
    assert deserialized_user == user_entity.dict()


def test_sign_up_use_case_check_if_email_is_available():
    entity = SignUpEmailEntity(email='lucas@domain.com')
    mock_repository = AuthenticationRepositoryInMemory(mock_all=True)
    use_case = SignUpUseCase(
        repository=mock_repository,
        password_manager=password_manager,
        email_provider=email_provider
    )

    assert use_case.check_if_email_is_available(email=entity) is True


def test_sign_up_use_case_user_register(user_entity_dict: Dict):
    user_entity = UserEntity(**user_entity_dict)
    use_case = SignUpUseCase(
        repository=repository,
        password_manager=password_manager,
        email_provider=email_provider
    )

    registered_user = use_case.user_register(user_entity=user_entity)

    assert registered_user.user_id is None
    assert registered_user.email == user_entity.email
    assert isinstance(registered_user.hash_password, bytes)


def test_sign_up_use_case_send_email(user_entity_dict: Dict):
    user_entity = UserEntity(**user_entity_dict)
    use_case = SignUpUseCase(
        repository=repository,
        password_manager=password_manager,
        email_provider=email_provider
    )

    assert use_case.send_email(user_entity=user_entity) is None


def test_sign_up_use_case_handler(sign_up_entity_dict: Dict):
    sign_up_entity = SignUpEntity(**sign_up_entity_dict)
    mock_repository = AuthenticationRepositoryInMemory(mock_all=True)
    use_case = SignUpUseCase(
        repository=mock_repository,
        password_manager=password_manager,
        email_provider=email_provider
    )

    registered_user = use_case.handler(entity=sign_up_entity)

    assert registered_user['user_id'] == 1
    assert registered_user['email'] == sign_up_entity.email
    assert isinstance(registered_user['hash_password'], bytes)
    assert registered_user['hash_password'] == sign_up_entity.password.encode()
    assert f'{registered_user["first_name"]} {registered_user["last_name"]}' == sign_up_entity.full_name
    assert registered_user['is_active'] is False
    assert registered_user['confirmation_code'] == 123


def test_sign_up_use_case_handler_user_email_is_active_must_raise_error(sign_up_entity_dict: Dict):
    sign_up_entity = SignUpEntity(**sign_up_entity_dict)
    mock_repository = AuthenticationRepositoryInMemory(mock_all=True)
    mock_repository.user_entity_mock.is_active = True
    use_case = SignUpUseCase(
        repository=mock_repository,
        password_manager=password_manager,
        email_provider=email_provider
    )

    with pytest.raises(Exception) as exc:
        use_case.handler(entity=sign_up_entity)

    assert str(exc.value) == 'email is not available'


def test_sign_up_confirmation_account_use_case_serialize_must_raise_not_implemented_error():
    use_case = SignUpConfirmationAccountUseCase(
        repository=repository,
        email_provider=email_provider
    )

    with pytest.raises(NotImplementedError):
        use_case.serialize()


def test_sign_up_confirmation_account_use_case_deserialize(user_entity_dict: Dict):
    user_entity = UserEntity(**user_entity_dict)
    use_case = SignUpConfirmationAccountUseCase(
        repository=repository,
        email_provider=email_provider
    )

    deserialized_user = use_case.deserialize(user_entity=user_entity)

    assert isinstance(deserialized_user, dict)
    assert deserialized_user == user_entity.dict()


def test_sign_up_confirmation_account_use_case_handler(sign_up_confirmation_account_entity_dict):
    entity = SignUpConfirmationAccountEntity(**sign_up_confirmation_account_entity_dict)
    mock_repository = AuthenticationRepositoryInMemory(mock_all=True)
    use_case = SignUpConfirmationAccountUseCase(
        repository=mock_repository,
        email_provider=email_provider
    )

    confirmed_user = use_case.handler(confirmation_entity=entity)

    assert confirmed_user['is_active'] is True


def test_sign_up_confirmation_account_use_case_handler_invalid_confirmation_code_must_raise_error(
        sign_up_confirmation_account_entity_dict: Dict
    ):
    entity = SignUpConfirmationAccountEntity(**sign_up_confirmation_account_entity_dict)
    entity.confirmation_code = 456
    mock_repository = AuthenticationRepositoryInMemory(mock_all=True)
    use_case = SignUpConfirmationAccountUseCase(
        repository=mock_repository,
        email_provider=email_provider
    )

    with pytest.raises(ValueError) as exc:
        use_case.handler(confirmation_entity=entity)

    assert str(exc.value) == 'incorrect confirmation code'
