from typing import *

from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams
from qdrant_client.conversions import common_types as types

from agarwood.databases.vector_db.base import BaseVectorDatabase


class QrantVectorDatabase(BaseVectorDatabase):
    def __init__(
            self,
            location: Optional[str] = None,
            url: Optional[str] = None,
            port: Optional[int] = 6333,
            grpc_port: int = 6334,
            prefer_grpc: bool = False,
            https: Optional[bool] = None,
            api_key: Optional[str] = None,
            prefix: Optional[str] = None,
            timeout: Optional[int] = None,
            host: Optional[str] = None,
            path: Optional[str] = None,
            metadata=Optional[Dict],
    ):
        self.client = QdrantClient(
            location=location,
            url=url,
            port=port,
            grpc_port=grpc_port,
            prefer_grpc=prefer_grpc,
            https=https,
            api_key=api_key,
            prefix=prefix,
            timeout=timeout,
            host=host,
            path=path,
            metadata=metadata,
        )

    def create_collection(self, collection_name: str, vectors_config: VectorParams):
        if not self.client.collection_exists(collection_name):
            self.client.create_collection(
                collection_name=collection_name,
                vectors_config=vectors_config,
            )

    def search(
            self,
            collection_name: str,
            query_vector: Union[
                Sequence[float],
                Tuple[str, List[float]],
                types.NamedVector,
                types.NamedSparseVector,
                types.NumpyArray,
            ],
            query_filter: Optional[types.Filter] = None,
            search_params: Optional[types.SearchParams] = None,
            limit: int = 10,
            offset: Optional[int] = None,
            with_payload: Union[bool, Sequence[str], types.PayloadSelector] = True,
            with_vectors: Union[bool, Sequence[str]] = False,
            score_threshold: Optional[float] = None,
            append_payload: bool = True,
            consistency: Optional[types.ReadConsistency] = None,
            shard_key_selector: Optional[types.ShardKeySelector] = None,
            timeout: Optional[int] = None,
            **kwargs: Any,

    ) -> List[types.ScoredPoint]:
        hits = self.client.search(
            collection_name=collection_name,
            query_vector=query_vector,
            query_filter=query_filter,
            search_params=search_params,
            limit=limit,
            offset=offset,
            with_payload=with_payload,
            with_vectors=with_vectors,
            score_threshold=score_threshold,
            append_payload=append_payload,
            consistency=consistency,
            shard_key_selector=shard_key_selector,
            timeout=timeout,
            **kwargs
        )
        return hits

    def insert(self, *args, **kwargs):
        ...

    def upload(self, *args, **kwargs):
        ...
