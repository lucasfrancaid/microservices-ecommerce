from abc import ABC, abstractmethod


class Controller(ABC):

    @abstractmethod
    def get(self):
        raise NotImplementedError

    @abstractmethod
    def post(self):
        raise NotImplementedError

    @abstractmethod
    def put(self):
        raise NotImplementedError

    @abstractmethod
    def patch(self):
        raise NotImplementedError

    @abstractmethod
    def delete(self):
        raise NotImplementedError
