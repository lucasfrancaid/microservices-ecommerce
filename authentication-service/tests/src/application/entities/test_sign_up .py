from typing import Dict

import pytest

from src.application.entities.sign_up import SignUpEntity, SignUpConfirmationAccountEntity
from src.application.entities.exceptions import SignUpEntityValidationError, SignUpConfirmationAccountEntityValidationError


def test_sign_up_entity(sign_up_entity_dict: Dict):
    sign_up_entity = SignUpEntity(**sign_up_entity_dict)

    assert sign_up_entity.__dict__ == sign_up_entity_dict


def test_sign_up_entity_invalid_email_should_raise_validation_error(sign_up_entity_dict: Dict):
    invalid_email = 'luc@s@entity.com.br'
    sign_up_entity_dict['email'] = invalid_email

    with pytest.raises(SignUpEntityValidationError) as exc:
        SignUpEntity(**sign_up_entity_dict)

    assert str(exc.value) == f'Email {invalid_email} is an invalid email'


def test_sign_up_entity_full_name_must_be_more_than_one_word(sign_up_entity_dict: Dict):
    sign_up_entity_dict['full_name'] = 'Lucas'

    with pytest.raises(SignUpEntityValidationError) as exc:
        SignUpEntity(**sign_up_entity_dict)

    assert str(exc.value) == 'Full name must be two words or more'


def test_sign_up_entity_password_length_must_be_equal_or_more_than_8_characters(sign_up_entity_dict: Dict):
    sign_up_entity_dict['password'] = 'Abc123'

    with pytest.raises(SignUpEntityValidationError) as exc:
        SignUpEntity(**sign_up_entity_dict)

    assert str(exc.value) == 'Password must be greater than or equal to 8 characters'


def test_sign_up_entity_password_and_password_confirmation_must_be_equal(sign_up_entity_dict: Dict):
    sign_up_entity_dict['password'] = 'MyPass1234'
    sign_up_entity_dict['password_confirmation'] = 'MyPass12345'

    with pytest.raises(SignUpEntityValidationError) as exc:
        SignUpEntity(**sign_up_entity_dict)

    assert str(exc.value) == 'Password and Password Confirmation must be equal'


def test_sign_up_confirmation_account_entity(sign_up_confirmation_account_entity_dict):
    confirmation_account_entity = SignUpConfirmationAccountEntity(**sign_up_confirmation_account_entity_dict)

    assert confirmation_account_entity.__dict__ == sign_up_confirmation_account_entity_dict


def test_sign_up_confirmation_account_entity_invalid_email_should_raise_validation_error(
    sign_up_confirmation_account_entity_dict: Dict
):
    invalid_email = 'luc@s@entity.com.br'
    sign_up_confirmation_account_entity_dict['email'] = invalid_email

    with pytest.raises(SignUpConfirmationAccountEntityValidationError) as exc:
        SignUpConfirmationAccountEntity(**sign_up_confirmation_account_entity_dict)

    assert str(exc.value) == f'Email {invalid_email} is an invalid email'
