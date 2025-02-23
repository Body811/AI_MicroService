from pydantic import BaseModel, Field
from typing import List, Dict

class StoreImageRequest(BaseModel):
    data: dict[str, str] = Field(
        ...,
        examples=[{
            "1": "https://example.com/image1.jpg",
            "2": "https://example.com/image2.jpg",
            "3": "https://example.com/image3.jpg"
            }]
        )
    
class StoreImageResponse(BaseModel):
    images_stored: int = Field(...,examples=[3])
    message: str = Field(..., examples=["Images Stored Successfully"])
    
class ImageSimilarityRequest(BaseModel):
    url: str = Field(..., examples=["https://example.com/image1.jpg"])
    top_k: int = Field(default=3, examples=[5])
    
class ImageSimilarityResponse(BaseModel):
    products: List[dict] = Field(
        ...,
        examples=[[
            {
                "id": "1",
                "url": "https://example.com/image1.jpg",
                "score": 0.95
            },
            {
                "id": "2",
                "url": "https://example.com/image2.jpg",
                "score": 0.93
            },
            {
                "id": "3",
                "url": "https://example.com/image3.jpg",
                "score": 0.90
            }
        ]]
    )

class deleteImageRequest(BaseModel):
    id: int
    
class deleteImageResponse(BaseModel):
    message: str