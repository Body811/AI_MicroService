from pydantic import BaseModel, Field
from typing import List
from uuid import UUID

class StoreImageRequest(BaseModel):
    data: dict[UUID, str] = Field(
        ...,
        examples=[{
            "550e8400-e29b-41d4-a716-446655440000": "https://example.com/image1.jpg",
            "3fa85f64-5717-4562-b3fc-2c963f66afa6": "https://example.com/image2.jpg",
            "16fd2706-8baf-433b-82eb-8c7fada847da": "https://example.com/image3.jpg"
            }]
        )
    
class StoreImageResponse(BaseModel):
    images_stored: int = Field(...,examples=[3])
    message: str = Field(..., examples=["Images Stored Successfully"])
    
    
class ImageSimilarityResponse(BaseModel):
    products: List[dict] = Field(
        ...,
        examples=[[
            {
                "id": "550e8400-e29b-41d4-a716-446655440000",
                "url": "https://example.com/image1.jpg",
                "score": 0.95
            },
            {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "url": "https://example.com/image2.jpg",
                "score": 0.93
            },
            {
                "id": "3",
                "url": "16fd2706-8baf-433b-82eb-8c7fada847da",
                "score": 0.90
            }
        ]]
    )

class DeleteImageRequest(BaseModel):
    ids: List[UUID]
    
class DeleteImageResponse(BaseModel):
    message: str