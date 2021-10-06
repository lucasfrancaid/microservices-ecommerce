from ast import literal_eval
from typing import Dict

import pytest
from pydantic import ValidationError

from service.core.entities.sign_up import SignUpEmailEntity, SignUpEntity, SignUpConfirmationAccountEntity


def test_sign_up_email_entity():
    email = 'lucas@entity.com.br'
    sign_up_email_entity = SignUpEmailEntity(email=email)

    assert sign_up_email_entity.email == email


def test_sign_up_email_entity_invalid_email_should_raise_validation_error():
    email = 'luc@s@entity.com.br'

    with pytest.raises(ValidationError) as exc:
        SignUpEmailEntity(email=email)

    error = literal_eval(exc.value.json())[0]

    assert error['loc'][0] == 'email'
    assert error['msg'] == 'value is not a valid email address'
    assert error['type'] == 'value_error.email'


def test_sign_up_entity_is_sign_up_email_entity_subclass():
    assert issubclass(SignUpEntity, SignUpEmailEntity)


def test_sign_up_entity_from_dict(sign_up_entity_dict: Dict):
    sign_up_entity = SignUpEntity(**sign_up_entity_dict)

    assert sign_up_entity.dict() == sign_up_entity_dict


def test_sign_up_entity_full_name_must_be_more_than_one_word(sign_up_entity_dict: Dict):
    sign_up_entity_dict['full_name'] = 'Lucas'

    with pytest.raises(ValidationError) as exc:
        SignUpEntity(**sign_up_entity_dict)

    error = literal_eval(exc.value.json())[0]

    assert error['loc'][0] == 'full_name'
    assert error['msg'] == 'Full name must be two words or more'
    assert error['type'] == 'value_error'


def test_sign_up_entity_password_length_must_be_equal_or_more_than_8_characters(sign_up_entity_dict: Dict):
    sign_up_entity_dict['password'] = 'Abc123'

    with pytest.raises(ValidationError) as exc:
        SignUpEntity(**sign_up_entity_dict)

    error = literal_eval(exc.value.json())[0]

    assert error['loc'][0] == 'password'
    assert error['msg'] == 'ensure this value has at least 8 characters'
    assert error['type'] == 'value_error.any_str.min_length'


def test_sign_up_entity_password_confirmation_length_must_be_equal_or_more_than_8_characters(sign_up_entity_dict: Dict):
    sign_up_entity_dict['password_confirmation'] = 'Abc123'

    with pytest.raises(ValidationError) as exc:
        SignUpEntity(**sign_up_entity_dict)

    error = literal_eval(exc.value.json())[0]

    assert error['loc'][0] == 'password_confirmation'
    assert error['msg'] == 'ensure this value has at least 8 characters'
    assert error['type'] == 'value_error.any_str.min_length'


def test_sign_up_entity_password_and_password_confirmation_must_be_equal(sign_up_entity_dict: Dict):
    sign_up_entity_dict['password'] = 'MyPass1234'
    sign_up_entity_dict['password_confirmation'] = 'MyPass12345'

    with pytest.raises(ValidationError) as exc:
        SignUpEntity(**sign_up_entity_dict)

    error = literal_eval(exc.value.json())[0]

    assert error['loc'][0] == 'password_confirmation'
    assert error['msg'] == 'Password and Password Confirmation must be equal'
    assert error['type'] == 'value_error'


def test_sign_up_confirmation_account_entity_is_sign_up_email_entity_subclass():
    assert issubclass(SignUpConfirmationAccountEntity, SignUpEmailEntity)


def test_sign_up_confirmation_account_entity(sign_up_confirmation_account_entity_dict):
    sign_up_confirmation_account_entity = SignUpConfirmationAccountEntity(**sign_up_confirmation_account_entity_dict)

    assert sign_up_confirmation_account_entity.dict() == sign_up_confirmation_account_entity_dict
