from src.application.security.token_manager import TokenManagerNone


class TokenManagerFactory:

    @staticmethod
    def none() -> TokenManagerNone:
        return TokenManagerNone()
