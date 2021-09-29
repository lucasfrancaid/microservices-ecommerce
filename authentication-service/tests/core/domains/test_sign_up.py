from ast import literal_eval
from typing import Dict

import pytest
from pydantic import ValidationError

from service.core.domains.sign_up import SignUpDomain


def test_sign_up_domain_from_dict(sign_up_dict: Dict):
    sign_up_domain = SignUpDomain(**sign_up_dict)

    assert sign_up_domain.dict() == sign_up_dict


def test_sign_up_domain_invalid_email(sign_up_dict: Dict):
    sign_up_dict['email'] = 'luc@s@domain.com.br'

    with pytest.raises(ValidationError) as exc:
        SignUpDomain(**sign_up_dict)

    error = literal_eval(exc.value.json())[0]

    assert error['loc'][0] == 'email'
    assert error['msg'] == 'value is not a valid email address'
    assert error['type'] == 'value_error.email'


def test_sign_up_domain_full_name_must_be_more_than_one_word(sign_up_dict: Dict):
    sign_up_dict['full_name'] = 'Lucas'

    with pytest.raises(ValidationError) as exc:
        SignUpDomain(**sign_up_dict)

    error = literal_eval(exc.value.json())[0]

    assert error['loc'][0] == 'full_name'
    assert error['msg'] == 'Full name must be two words or more'
    assert error['type'] == 'value_error'


def test_sign_up_domain_password_length_must_be_equal_or_more_than_8_characters(sign_up_dict: Dict):
    sign_up_dict['password'] = 'Abc123'

    with pytest.raises(ValidationError) as exc:
        SignUpDomain(**sign_up_dict)

    error = literal_eval(exc.value.json())[0]

    assert error['loc'][0] == 'password'
    assert error['msg'] == 'ensure this value has at least 8 characters'
    assert error['type'] == 'value_error.any_str.min_length'


def test_sign_up_domain_password_confirmation_length_must_be_equal_or_more_than_8_characters(sign_up_dict: Dict):
    sign_up_dict['password_confirmation'] = 'Abc123'

    with pytest.raises(ValidationError) as exc:
        SignUpDomain(**sign_up_dict)

    error = literal_eval(exc.value.json())[0]

    assert error['loc'][0] == 'password_confirmation'
    assert error['msg'] == 'ensure this value has at least 8 characters'
    assert error['type'] == 'value_error.any_str.min_length'


def test_sign_up_domain_password_and_password_confirmation_must_be_equal(sign_up_dict: Dict):
    sign_up_dict['password'] = 'MyPass1234'
    sign_up_dict['password_confirmation'] = 'MyPass12345'

    with pytest.raises(ValidationError) as exc:
        SignUpDomain(**sign_up_dict)

    error = literal_eval(exc.value.json())[0]

    assert error['loc'][0] == 'password_confirmation'
    assert error['msg'] == 'Password and Password Confirmation must be equal'
    assert error['type'] == 'value_error'
