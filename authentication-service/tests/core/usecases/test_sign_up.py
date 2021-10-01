from typing import Dict

from service.core.entities.user import UserEntity
from service.core.entities.sign_up import SignUpEmailEntity, SignUpEntity
from service.core.usecases.sign_up import SignUpUseCase
from service.core.repositories.authentication import AuthenticationRepositoryNone
from service.core.security.password_manager import PasswordManagerNone

repository = AuthenticationRepositoryNone()
password_manager = PasswordManagerNone()


def test_sign_up_use_case_check_if_email_is_available():
    entity = SignUpEmailEntity(email='lucas@domain.com')
    use_case = SignUpUseCase(repository=repository, password_manager=password_manager)

    assert use_case.check_if_email_is_available(email_entity=entity) is False


def test_sign_up_use_case_serialize(sign_up_entity_dict: Dict):
    sign_up_entity = SignUpEntity(**sign_up_entity_dict)
    use_case = SignUpUseCase(repository=repository, password_manager=password_manager)

    serialized_user: UserEntity = use_case.serialize(entity=sign_up_entity)

    assert serialized_user.user_id is None
    assert f'{serialized_user.first_name} {serialized_user.last_name}' == sign_up_entity.full_name
    assert serialized_user.email == sign_up_entity.email
    assert serialized_user.hash_password == sign_up_entity.password.encode()
    assert serialized_user.is_active is False
    assert serialized_user.confirmation_code is None


def test_sign_up_use_case_user_register(user_entity_dict: Dict):
    user_entity = UserEntity(**user_entity_dict)
    use_case = SignUpUseCase(repository=repository, password_manager=password_manager)

    registered_user = use_case.user_register(user_entity=user_entity)

    assert registered_user.user_id is None
    assert registered_user.email == user_entity.email
    assert isinstance(registered_user.hash_password, bytes)


def test_sign_up_use_case_handler(sign_up_entity_dict: Dict):
    sign_up_entity = SignUpEntity(**sign_up_entity_dict)
    use_case = SignUpUseCase(repository=repository, password_manager=password_manager)

    registered_user = use_case.handler(entity=sign_up_entity)

    assert registered_user['user_id'] is None
    assert registered_user['email'] == sign_up_entity.email
    assert isinstance(registered_user['hash_password'], bytes)
    assert registered_user['hash_password'] == sign_up_entity.password.encode()
    assert f'{registered_user["first_name"]} {registered_user["last_name"]}' == sign_up_entity.full_name
    assert registered_user['is_active'] is False
    assert registered_user['confirmation_code'] is None
