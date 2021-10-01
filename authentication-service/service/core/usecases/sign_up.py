from typing import Dict

from service.core.entities.user import UserEntity
from service.core.entities.sign_up import SignUpEmailEntity, SignUpEntity
from service.core.repositories.authentication import AuthenticationRepository
from service.core.security.password_manager import PasswordManager


class SignUpUseCase:

    def __init__(
        self,
        repository: AuthenticationRepository,
        password_manager: PasswordManager,
    ) -> None:
        self.repository: AuthenticationRepository = repository
        self.password_manager: PasswordManager = password_manager

    def check_if_email_is_available(self, email_entity: SignUpEmailEntity) -> bool:
        user = self.repository.get(email=email_entity)
        return True if user else False

    def handler(self, entity: SignUpEntity) -> Dict:
        serialized_user = self.serialize(entity=entity)
        user = self.user_register(serialized_user)
        self.send_email(user)
        return user.dict()

    def serialize(self, entity: SignUpEntity) -> UserEntity:
        delimiter = ' '
        first_name, *last_name = entity.full_name.split(delimiter)
        hash_password = self.password_manager.hash(password=entity.password)
        user = UserEntity(
            first_name=first_name,
            last_name=delimiter.join(last_name),
            email=entity.email,
            hash_password=hash_password
        )
        return user

    def user_register(self, user: UserEntity) -> UserEntity:
        registered_user = self.repository.create(user)
        # Mock return
        registered_user = user
        registered_user.user_id = 1
        return registered_user

    def send_email(self, user: UserEntity) -> None:
        print('--> Email was sent!')
