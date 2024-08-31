from abc import ABC, abstractmethod


class BaseCacheDataBase(ABC):

    @abstractmethod
    def get(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def set(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def delete(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def clear(self, *args, **kwargs):
        raise NotImplementedError
