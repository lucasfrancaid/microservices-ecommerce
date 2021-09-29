from typing import Dict

from service.core.entities.user import UserEntity
from service.core.entities.sign_up import SignUpEmailEntity, SignUpEntity
from service.core.repositories.authentication import AuthenticationRepository


class SignUpUseCase:

    def __init__(
        self,
        repository: AuthenticationRepository,
        entity: SignUpEntity = None,
        email_entity: SignUpEmailEntity = None
    ) -> None:
        self.repository: AuthenticationRepository = repository
        self.entity: SignUpEntity = entity
        self.email_entity: SignUpEmailEntity = email_entity

    def check_if_email_is_available(self) -> bool:
        user = self.repository.get(email=self.email_entity)
        return True if user else False

    def handler(self) -> Dict:
        serialized_user = self.serialize()
        user = self.user_register(serialized_user)
        self.send_email(user)
        return user.dict()

    def serialize(self) -> UserEntity:
        delimiter = ' '
        first_name, *last_name = self.entity.full_name.split(delimiter)
        # Hash password
        user = UserEntity(
            first_name=first_name,
            last_name=delimiter.join(last_name),
            email=self.entity.email,
            hash_password=self.entity.password.encode()
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
