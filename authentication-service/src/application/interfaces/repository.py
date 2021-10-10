from abc import ABC, abstractmethod


class Repository(ABC):

    @abstractmethod
    def all(self):
        raise NotImplementedError

    @abstractmethod
    def get(self):
        raise NotImplementedError

    @abstractmethod
    def create(self):
        raise NotImplementedError

    @abstractmethod
    def update(self):
        raise NotImplementedError

    @abstractmethod
    def delete(self):
        raise NotImplementedError
