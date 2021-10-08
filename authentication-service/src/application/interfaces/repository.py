from abc import ABC, abstractmethod


class Repository(ABC):

    @abstractmethod
    def __init__(*args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def all(*args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def get(*args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def create(*args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def update(*args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def delete(*args, **kwargs):
        raise NotImplementedError
