from fastapi import APIRouter, HTTPException
from app.services.image_similarity_service import store_image_embeddings, find_similar
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


@router.post("/search",response_model=ImageSimilarityResponse)
async def search_image(request: ImageSimilarityRequest):
    try:
        results = await find_similar(request.url, request.top_k)
        return ImageSimilarityResponse(products=results)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




#TODO Endpoint save Embedding: (list of urls) -> returns message (DONE)
#TODO Endpoint get closest item: (1 url) -> returns list of product ids (DONE)
#TODO Endpoint to delete an item: (id) -> returns message
#TODO Endpoint that returns all saved embeddings: () -> list of all embeddings with its payload
#TODO Endpoint that searches for a specific id: (id) -> returns the saved embedding and payload