from agarwood.databases.cache_db.base import BaseCacheDataBase


class RedisCacheDataBase(BaseCacheDataBase):
    def __init__(self):
        super().__init__()

    def get(self, *args, **kwargs):
        raise NotImplementedError

    def set(self, *args, **kwargs):
        raise NotImplementedError

    def delete(self, *args, **kwargs):
        raise NotImplementedError

    def clear(self, *args, **kwargs):
        raise NotImplementedError
