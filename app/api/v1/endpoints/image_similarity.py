from fastapi import APIRouter, HTTPException, UploadFile, File
from services.image_similarity_service import store_image_service, search_image_service, delete_image_service
from api.v1.models.image_similarity import *

router = APIRouter()

@router.post("/add", response_model=StoreImageResponse)
async def store_images(request: StoreImageRequest):
    try:
        allowed_extensions = ["jpg", "jpeg", "png", "webp"]
        for image_id, image_url in request.data.items():
            extension = image_url.split(".")[-1].lower()
        
        if extension not in allowed_extensions:
                raise HTTPException(
                    status_code=400, 
                    detail=f"Image format '{extension}' is not supported. Only {', '.join(allowed_extensions)} formats are allowed."
                )
                
        stored_images = await store_image_service(request.data)    
        return StoreImageResponse(
            images_stored=stored_images,
            message="Images Stored Successfully"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/search",response_model=ImageSimilarityResponse)
async def search_image(file: UploadFile = File(...),top_k: int = 5):
    """
    Search for similar images based on the uploaded image.
    ### Parameters:
    - file: The image file to search for similar images.
    - top_k: The number of similar images to return (default is 5).
    ### Notes:
    - Supported image formats: JPG, PNG, WebP, JPEG.
    """
    try:
        allowed_extensions = ["jpg", "jpeg", "png", "webp"]
        if file.content_type not in allowed_extensions:
            raise HTTPException(status_code=400, detail="Invalid file type!: Use supported formats (jpg, jpeg, png, webp)")
        
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
    
    
