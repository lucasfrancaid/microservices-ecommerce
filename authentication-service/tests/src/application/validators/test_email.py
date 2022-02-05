import pytest

from src.application.validators.email import EmailValidator, EmailValidatorError


def test_email_validator_validate_email():
    email = 'lucas@email.com'

    assert EmailValidator.validate_email(email)


def test_email_validator_validate_email_invalid_email_should_raise_validator_error():
    email = 'luc@s@email.com.br'
    another_email = 'lucas.email.com.br'

    with pytest.raises(EmailValidatorError) as exc_email:
        EmailValidator.validate_email(email)

    with pytest.raises(EmailValidatorError) as exc_another_email:
        EmailValidator.validate_email(another_email)

    assert str(exc_email.value) == f'Email {email} is an invalid email'
    assert str(exc_another_email.value) == f'Email {another_email} is an invalid email'
