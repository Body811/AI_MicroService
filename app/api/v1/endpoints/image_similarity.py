from fastapi import APIRouter, HTTPException, UploadFile, File
from app.services.image_similarity_service import store_image_service, search_image_service, delete_image_service
from app.api.v1.models.image_similarity import *

router = APIRouter()

@router.post("/store", response_model=StoreImageResponse)
async def store_images(request: StoreImageRequest):
    try:
        stored_images = await store_image_service(request.data)    
        return StoreImageResponse(
            images_stored=stored_images,
            message="Images Stored Successfully"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/search",response_model=ImageSimilarityResponse)
async def search_image(file: UploadFile = File(...),top_k: int = 5):
    try:
        if file.content_type not in {"image/jpg, image/png, image/webp"}:
            raise HTTPException(status_code=400, detail="Invalid file type!: Use supported formats (jpg, png, webp)")
        
        results = await search_image_service(file, top_k)
        return ImageSimilarityResponse(images=results)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.delete("/delete",response_model=DeleteImageResponse)
async def delete_image(request: DeleteImageRequest):
    try:
        
        delete_image_service(request.ids)
        return DeleteImageResponse(
            message=f"Deleted {len(request.ids)} items successfully"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
