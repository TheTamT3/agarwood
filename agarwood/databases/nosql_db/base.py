from abc import ABC, abstractmethod


class BaseNoSQLDatabase(ABC):

    @abstractmethod
    def insert(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def find(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def update(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def delete(self, *args, **kwargs):
        raise NotImplementedError
