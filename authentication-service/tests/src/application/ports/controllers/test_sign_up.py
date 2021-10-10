from typing import Dict

import pytest

from src.domain.entities.user import UserEntity
from src.application.entities.sign_up import SignUpEntity, SignUpConfirmationAccountEntity
from src.application.ports.controllers.sign_up import SignUpController
from src.application.ports.repositories.authentication import AuthenticationRepositoryInMemory
from src.application.security.password_manager import PasswordManagerFake
from src.application.services.email import EmailServiceFake


def test_sign_up_controller_post_method(sign_up_entity_dict: Dict):
    controller = SignUpController()

    response = controller.post(
        repository=AuthenticationRepositoryInMemory(),
        password_manager=PasswordManagerFake(),
        email_service=EmailServiceFake(),
        entity=SignUpEntity(**sign_up_entity_dict),
    )

    assert isinstance(response, dict)
    assert UserEntity(**response)


def test_sign_up_controller_put_method(sign_up_confirmation_account_entity_dict: Dict, user_entity_dict: Dict):
    controller = SignUpController()
    repository = AuthenticationRepositoryInMemory()
    entity = SignUpConfirmationAccountEntity(**sign_up_confirmation_account_entity_dict)

    user_entity = UserEntity(**user_entity_dict)
    user_entity.user_id = 999
    user_entity.email = entity.email
    user_entity.is_active = False
    user_entity.confirmation_code = entity.confirmation_code
    repository.storage.data.append(user_entity)

    response = controller.put(
        repository=repository,
        email_service=EmailServiceFake(),
        entity=entity,
    )

    assert isinstance(response, dict)
    assert UserEntity(**response)


def test_sign_up_controller_get_not_implemented():
    with pytest.raises(NotImplementedError):
        SignUpController().get()


def test_sign_up_controller_patch_not_implemented():
    with pytest.raises(NotImplementedError):
        SignUpController().patch()


def test_sign_up_controller_delete_not_implemented():
    with pytest.raises(NotImplementedError):
        SignUpController().delete()
