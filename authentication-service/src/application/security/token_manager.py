from abc import ABC, abstractmethod
from typing import Dict


class TokenManager(ABC):

    @abstractmethod
    def build(self, data: Dict = None) -> str:
        raise NotImplementedError

    @abstractmethod
    def refresh(self, refresh_token: str = None) -> str:
        raise NotImplementedError

    def validate(self, token: str = None) -> bool:
        raise NotImplementedError

    def get_data(self, token: str = None) -> Dict:
        raise NotImplementedError


class TokenManagerNone(TokenManager):

    def build(self, data: Dict = None) -> None:
        pass

    def refresh(self, refresh_token: str = None) -> None:
        pass

    def validate(self, token: str = None) -> None:
        pass

    def get_data(self, token: str = None) -> None:
        pass
