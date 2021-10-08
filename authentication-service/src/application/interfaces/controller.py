from abc import ABC, abstractmethod


class Controller(ABC):

    @abstractmethod
    def __init__(*args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def get(*args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def post(*args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def put(*args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def patch(*args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def delete(*args, **kwargs):
        raise NotImplementedError
