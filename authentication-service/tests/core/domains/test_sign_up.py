import copy
from ast import literal_eval

import pytest
from pydantic import ValidationError

from service.core.domains.sign_up import SignUpDomain

pytest.sign_up_dict_mock = {
    'full_name': 'Lucas França',
    'email': 'lucas@domain.com',
    'password': 'MyPass123',
    'confirm_password': 'MyPass123',
}


def test_sign_up_domain_from_dict():
    sign_up_domain = SignUpDomain(**pytest.sign_up_dict_mock)
    assert pytest.sign_up_dict_mock == sign_up_domain.dict()


def test_sign_up_domain_full_name_must_be_more_than_one_word():
    sign_up_dict = copy.deepcopy(pytest.sign_up_dict_mock)
    sign_up_dict['full_name'] = 'Lucas'
    with pytest.raises(ValidationError) as exc:
        SignUpDomain(**sign_up_dict)
        error = literal_eval(exc.value.json())[0]
        assert error['loc'][0] == 'full_name'
        assert error['msg'] == 'Full name must be two words or more'
        assert error['type'] == 'value_error'
