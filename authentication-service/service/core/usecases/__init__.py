from abc import ABC, abstractmethod


class UseCase(ABC):

    @abstractmethod
    def handler(*args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def serialize(*args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def deserialize(*args, **kwargs):
        raise NotImplementedError
