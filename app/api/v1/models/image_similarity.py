from pydantic import BaseModel, Field
from typing import List, Dict

class StoreImageRequest(BaseModel):
    data: Dict[int, str] = Field(
        ...,
        examples=[{
            1: "https://example.com/image1.jpg",
            2: "https://example.com/image2.jpg",
            3: "https://example.com/image3.jpg"
            }]
        )
    
class StoreImageResponse(BaseModel):
    images_stored: int = Field(...,examples=[3])
    message: str = Field(..., examples=["Images Stored Successfully"])
    
class ImageSimilarityRequest(BaseModel):
    url: str
    top_k: int
    
class ImageSimilarityResponse(BaseModel):
    products: List[str]

class deleteImageRequest(BaseModel):
    id: int
    
class deleteImageResponse(BaseModel):
    message: str