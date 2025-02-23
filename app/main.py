from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.v1.endpoints import image_similarity, product_recommendation
from app.core.config import settings
from app.core.qdrant_utils import qdrant_client, create_qdrant_collection


@asynccontextmanager
async def lifespan(app: FastAPI):
    collection_name = settings.QDRANT_SIMILARITY_COLLECTION_NAME
    vector_size = settings.QDRANT_SIMILARITY_COLLECTION_VECTOR_SIZE
    if not qdrant_client.collection_exists(collection_name=collection_name):
        create_qdrant_collection(collection_name=collection_name, vector_size=vector_size)
        print(f"Created Qdrant collection: {collection_name}")
    else:
        print(f"Qdrant collection '{collection_name}' already exists.")

    yield  # App runs here

    print("FastAPI shutting down")



app = FastAPI(title=settings.APP_NAME, version="1.0.0",lifespan=lifespan)

app.include_router(image_similarity.router, prefix="/api/v1/similarity", tags=["image_similarity"])
# app.include_router(product_recommendation.router, prefix="/api/v1/recommendation", tags=["product_recommendation"])


