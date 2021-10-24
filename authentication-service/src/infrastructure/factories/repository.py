from src.application.ports.repositories.authentication import AuthenticationRepositoryInMemory


class RepositoryFactory:

    @staticmethod
    def in_memory() -> AuthenticationRepositoryInMemory:
        return AuthenticationRepositoryInMemory()
