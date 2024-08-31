from agarwood.databases.nosql_db.base import BaseNoSQLDatabase


class MongoDataBase(BaseNoSQLDatabase):
    def __init__(self):
        super().__init__()

    def insert(self, *args, **kwargs):
        raise NotImplementedError

    def find(self, *args, **kwargs):
        raise NotImplementedError

    def update(self, *args, **kwargs):
        raise NotImplementedError

    def delete(self, *args, **kwargs):
        raise NotImplementedError
