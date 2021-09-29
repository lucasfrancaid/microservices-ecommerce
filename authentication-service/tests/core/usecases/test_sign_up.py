from typing import Dict

from pydantic.types import _registered

from service.core.entities.user import UserEntity
from service.core.entities.sign_up import SignUpEmailEntity, SignUpEntity
from service.core.usecases.sign_up import SignUpUseCase
from service.core.repositories.authentication import AuthenticationRepositoryNone

repository = AuthenticationRepositoryNone()


def test_sign_up_use_case_check_if_email_is_available():
    entity = SignUpEmailEntity(email='lucas@domain.com')
    use_case = SignUpUseCase(repository=repository, email_entity=entity)

    assert use_case.check_if_email_is_available() is False


def test_sign_up_use_case_serialize(sign_up_entity_dict: Dict):
    sign_up_entity = SignUpEntity(**sign_up_entity_dict)
    use_case = SignUpUseCase(repository=repository, entity=sign_up_entity)

    serialized_user = use_case.serialize()

    assert serialized_user.user_id is None
    assert f'{serialized_user.first_name} {serialized_user.last_name}' == sign_up_entity.full_name
    assert serialized_user.email == sign_up_entity.email
    assert serialized_user.hash_password == sign_up_entity.password.encode()
    assert serialized_user.is_active is False
    assert serialized_user.confirmation_code is None


def test_sign_up_use_case_handler(sign_up_entity_dict: Dict):
    entity = SignUpEntity(**sign_up_entity_dict)
    use_case = SignUpUseCase(repository=repository, entity=entity)

    registered_user = use_case.handler()

    assert registered_user['user_id'] == 1
    assert registered_user['email'] == entity.email
    assert isinstance(registered_user['hash_password'], bytes)
