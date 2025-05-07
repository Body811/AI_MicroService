from pydantic import BaseModel, Field
from typing import List, Dict
# from uuid import UUID

class StoreImageRequest(BaseModel):
    data: Dict[str, str] = Field(
        ...,
        description="Dictionary mapping product UUIDs to image URLs",
        examples=[{
            "550e8400-e29b-41d4-a716-446655440000": "https://example.com/image1.jpg",
            "3fa85f64-5717-4562-b3fc-2c963f66afa6": "https://example.com/image2.jpg",
            "16fd2706-8baf-433b-82eb-8c7fada847da": "https://example.com/image3.jpg"
        }]
    )
    
    class Config:
        schema_extra = {
            "example": {
                "data": {
                    "550e8400-e29b-41d4-a716-446655440000": "https://example.com/wooden-bowl.jpg",
                    "3fa85f64-5717-4562-b3fc-2c963f66afa6": "https://example.com/wool-scarf.jpg",
                    "16fd2706-8baf-433b-82eb-8c7fada847da": "https://example.com/ceramic-mug.jpg"
                }
            }
        }
    
class StoreImageResponse(BaseModel):
    images_stored: int = Field(
        ...,
        description="Number of images successfully stored",
        examples=[3]
    )
    message: str = Field(
        ..., 
        description="Status message about the storage operation",
        examples=["Images Stored Successfully"]
    )
    
    class Config:
        schema_extra = {
            "example": {
                "images_stored": 3,
                "message": "Images Stored Successfully"
            }
        }

class ImageSimilarity(BaseModel):
    id: UUID = Field(
        ...,
        description="Unique identifier of the image",
        examples=["550e8400-e29b-41d4-a716-446655440000"]
    )
    url: str = Field(
        ...,
        description="URL where the image can be accessed",
        examples=["https://example.com/wooden-bowl.jpg"]
    )
    score: float = Field(
        ...,
        description="Similarity score (higher means more similar)",
        examples=[0.95],
        ge=0.0,
        le=1.0
    )
    
    class Config:
        schema_extra = {
            "example": {
                "id": "550e8400-e29b-41d4-a716-446655440000",
                "url": "https://example.com/wooden-bowl.jpg",
                "score": 0.95
            }
        }
   
class ImageSimilarityResponse(BaseModel):
    images: List[ImageSimilarity] = Field(
        ...,
        description="List of similar images with their scores"
    )
    
    class Config:
        schema_extra = {
            "example": {
                "images": [
                    {
                        "id": "550e8400-e29b-41d4-a716-446655440000",
                        "url": "https://example.com/wooden-bowl.jpg",
                        "score": 0.95
                    },
                    {
                        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                        "url": "https://example.com/similar-bowl.jpg",
                        "score": 0.93
                    },
                    {
                        "id": "16fd2706-8baf-433b-82eb-8c7fada847da",
                        "url": "https://example.com/wooden-platter.jpg",
                        "score": 0.90
                    }
                ]
            }
        }

class DeleteImageRequest(BaseModel):
    ids: List[UUID] = Field(
        ...,
        description="List of image IDs to delete",
        examples=[["550e8400-e29b-41d4-a716-446655440000", "3fa85f64-5717-4562-b3fc-2c963f66afa6"]]
    )
    
    class Config:
        schema_extra = {
            "example": {
                "ids": [
                    "550e8400-e29b-41d4-a716-446655440000",
                    "3fa85f64-5717-4562-b3fc-2c963f66afa6"
                ]
            }
        }
   
class DeleteImageResponse(BaseModel):
    images_deleted: int = Field(
        ...,
        description="Number of images successfully deleted",
        examples=[2]
    )
    message: str = Field(
        ...,
        description="Status message about the deletion operation",
        examples=["Images Deleted Successfully"]
    )
    
    class Config:
        schema_extra = {
            "example": {
                "images_deleted": 2,
                "message": "Images Deleted Successfully"
            }
        }