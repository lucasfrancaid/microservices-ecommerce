from src.application.services.email import EmailServiceNone


class EmailServiceFactory:

    @staticmethod
    def none() -> EmailServiceNone:
        return EmailServiceNone()
