from fastapi import FastAPI
import torch
from contextlib import asynccontextmanager
from api.v1.endpoints import image_similarity, product_recommendation
from core.config import settings
from core.qdrant_utils import qdrant_client, create_qdrant_collection

torch.backends.nnpack.enabled = False
torch.set_default_dtype(torch.float32)

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    image_collection_name = settings.QDRANT_SIMILARITY_COLLECTION_NAME
    image_vector_size = settings.QDRANT_SIMILARITY_COLLECTION_VECTOR_SIZE
    if not qdrant_client.collection_exists(collection_name=image_collection_name):
        create_qdrant_collection(collection_name=image_collection_name, vector_size=image_vector_size)
        print(f"FastAPI:: Created Qdrant collection: {image_collection_name}")
    else:
        print(f"FastAPI:: Qdrant collection '{image_collection_name}' already exists.")
        

    product_collection_name = settings.QDRANT_RECOMMENDATION_COLLECTION_NAME
    product_vector_size = settings.QDRANT_RECOMMENDATION_COLLECTION_VECTOR_SIZE

    if not qdrant_client.collection_exists(collection_name=product_collection_name):
        create_qdrant_collection(
            collection_name=product_collection_name,
            vector_size=product_vector_size
        )
        print(f"FastAPI:: Created Qdrant collection: {product_collection_name}")
    else:
        print(f"FastAPI:: Qdrant collection '{product_collection_name}' already exists.")
    
    yield  

    print("FastAPI:: shutting down")



app = FastAPI(title=settings.APP_NAME, version="1.0.0",lifespan=lifespan)

app.include_router(image_similarity.router, prefix="/api/v1/image", tags=["image_similarity"])
app.include_router(product_recommendation.router, prefix="/api/v1/product", tags=["product_recommendation"])


