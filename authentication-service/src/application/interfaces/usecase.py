from abc import ABC, abstractmethod


class UseCase(ABC):

    @abstractmethod
    def handler(self):
        raise NotImplementedError

    @abstractmethod
    def serialize(self):
        raise NotImplementedError

    @abstractmethod
    def deserialize(self):
        raise NotImplementedError
