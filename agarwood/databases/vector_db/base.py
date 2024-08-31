from abc import ABC, abstractmethod


class BaseVectorDatabase(ABC):

    @abstractmethod
    def search(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def add(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def upload(self, *args, **kwargs):
        raise NotImplementedError
