from src.application.services.email import EmailServiceFake


class EmailServiceFactory:

    @staticmethod
    def fake() -> EmailServiceFake:
        return EmailServiceFake()
