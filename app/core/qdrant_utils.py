from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

from app.core.config import settings

qdrant_client = QdrantClient(url=settings.QDRANT_URL, api_key=settings.QDRANT_API_KEY)



def create_qdrant_collection(collection_name: str, vector_size: int):


    qdrant_client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
    )
