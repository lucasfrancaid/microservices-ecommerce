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
        user_entity = self.user_register(user_entity=serialized_user)
        self.send_email(user_entity)
        return user_entity.dict()

    def serialize(self, entity: SignUpEntity) -> UserEntity:
        delimiter = ' '
        first_name, *last_name = entity.full_name.split(delimiter)
        hash_password = self.password_manager.hash(password=entity.password)
        user_entity = UserEntity(
            first_name=first_name,
            last_name=delimiter.join(last_name),
            email=entity.email,
            hash_password=hash_password
        )
        return user_entity

    def user_register(self, user_entity: UserEntity) -> UserEntity:
        registered_user = self.repository.create(entity=user_entity)
        # Mock return
        registered_user = user_entity
        registered_user.user_id = 1
        return registered_user

    def send_email(self, user_entity: UserEntity) -> None:
        print('--> Email was sent!')
