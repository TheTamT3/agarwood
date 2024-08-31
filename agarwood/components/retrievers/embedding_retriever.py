from agarwood.components.retrievers.base import BaseRetriever
from agarwood.databases.vector_db.base import BaseVectorDatabase


class EmbeddingRetriever(BaseRetriever):
    def __init__(self, store: BaseVectorDatabase):
        self.store = store

    def _retrieve(self, *args, **kwargs):
        result = self.store.search(*args, **kwargs)
        return result