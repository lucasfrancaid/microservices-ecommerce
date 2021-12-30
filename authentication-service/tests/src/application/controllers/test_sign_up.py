from typing import Dict

import pytest

from src.application.entities.sign_up import SignUpEntity, SignUpConfirmationAccountEntity
from src.application.controllers.sign_up import SignUpController
from src.domain.entities.user import UserEntity
from src.infrastructure.factories.app import ApplicationFactory


@pytest.mark.asyncio
async def test_sign_up_controller_post_method(fake_factory: ApplicationFactory, sign_up_entity_dict: Dict):
    controller = SignUpController()

    response = await controller.post(
        repository=fake_factory.repository,
        password_manager=fake_factory.password_manager,
        email_service=fake_factory.email_service,
        entity=SignUpEntity(**sign_up_entity_dict),
    )

    assert isinstance(response, dict)
    assert UserEntity(**response)


@pytest.mark.asyncio
async def test_sign_up_controller_put_method(
    fake_factory: ApplicationFactory, sign_up_confirmation_account_entity_dict: Dict, user_entity_dict: Dict
):
    controller = SignUpController()
    entity = SignUpConfirmationAccountEntity(**sign_up_confirmation_account_entity_dict)

    user_entity = UserEntity(**user_entity_dict)
    user_entity.user_id = 999
    user_entity.email = entity.email
    user_entity.is_active = False
    user_entity.confirmation_code = entity.confirmation_code
    fake_factory.repository.storage.data.append(user_entity)

    response = await controller.put(
        repository=fake_factory.repository,
        email_service=fake_factory.email_service,
        entity=entity,
    )

    assert isinstance(response, dict)
    assert UserEntity(**response)


@pytest.mark.asyncio
async def test_sign_up_controller_get_not_implemented():
    with pytest.raises(NotImplementedError):
        SignUpController().get()


@pytest.mark.asyncio
async def test_sign_up_controller_patch_not_implemented():
    with pytest.raises(NotImplementedError):
        SignUpController().patch()


@pytest.mark.asyncio
async def test_sign_up_controller_delete_not_implemented():
    with pytest.raises(NotImplementedError):
        SignUpController().delete()
