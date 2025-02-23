from fastapi import APIRouter, HTTPException
from app.services.image_similarity_service import store_image_embeddings
from app.api.v1.models.image_similarity import *

router = APIRouter()

@router.post("/store", response_model=StoreImageResponse)
async def store_images(request: StoreImageRequest):
    try:
        stored_images = await store_image_embeddings(request.data)    
        return StoreImageResponse(
            images_stored=stored_images,
            message="Images Stored Successfully"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    

#TODO Endpoint save Embedding: (list of urls) -> saves vector embedding to Qdrant 
#TODO Endpoint get closest item: (1 url) -> returns list of product ids