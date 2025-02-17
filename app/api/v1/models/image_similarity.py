from pydantic import BaseModel
from typing import List

class StoreImageRequest(BaseModel):
    url: List[str]
    
class StoreImageResponse(BaseModel):
    images_stored: int
    message: str
    
class getImageSimilarityRequest(BaseModel):
    url: str
    topk: int
    
class getImageSimilarityResponse(BaseModel):
    products: List[str]
    