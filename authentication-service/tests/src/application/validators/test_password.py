import pytest

from src.application.validators.password import PasswordValidator, PasswordValidatorError


def test_password_validator_validate_password_rules():
    password = 'Abcd1234!'

    assert PasswordValidator.validate_password_rules(password)


def test_password_validator_validate_password_rules_password_must_be_equal_or_more_than_8_characters():
    password = 'Abc123'

    with pytest.raises(PasswordValidatorError) as exc:
        PasswordValidator.validate_password_rules(password)

    assert str(exc.value) == 'Password must be greater than or equal to 8 characters'


def test_password_validator_validate_password_confirmation():
    password = 'MyPass1234'
    password_confirmation = 'MyPass1234'

    assert PasswordValidator.validate_password_confirmation(password, password_confirmation)


def test_password_validator_validate_password_confirmation_passwords_must_be_equal():
    password = 'MyPass1234'
    password_confirmation = 'MyPass12345'

    with pytest.raises(PasswordValidatorError) as exc:
        PasswordValidator.validate_password_confirmation(password, password_confirmation)

    assert str(exc.value) == 'Password and Password Confirmation must be equal'
