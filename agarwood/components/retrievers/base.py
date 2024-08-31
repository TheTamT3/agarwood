from abc import ABC, abstractmethod


class BaseRetriever(ABC):

    @abstractmethod
    def _retrieve(self, *args, **kwargs):
        raise NotImplementedError

    def retrieve(self, *args, **kwargs):
        return self._retrieve(*args, **kwargs)
