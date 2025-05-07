from pydantic import BaseModel, Field
from typing import List


class Product(BaseModel):
    product_id: str = Field(..., examples=["123e4567-e89b-12d3-a456-426614174000"])
    name: str = Field(..., examples=["Handcrafted Wooden Bowl"])
    description: str = Field(...,examples=["Beautiful hand-carved wooden bowl made from sustainable oak. Perfect as a centerpiece or for serving salads."],)
    handcrafter_name: str = Field(..., examples=["Jane Carpenter"])
    categories: List[str] = Field(..., examples=[["wood", "home decor", "crafts"]])
    price: float = Field(..., examples=[42.99])
    average_rating: float = Field(..., examples=[4.8])


class StoreProductRequest(BaseModel):
    products: List[Product] = Field(...,description="List of products to store in the recommendation system")

    class Config:
            schema_extra = {
                "example": {
                    "products": [
                        {
                            "product_id": "123e4567-e89b-12d3-a456-426614174000",
                            "name": "Handcrafted Wooden Bowl",
                            "description": "Beautiful hand-carved wooden bowl made from sustainable oak.",
                            "handcrafter_name": "Jane Carpenter",
                            "categories": ["kitchen", "home decor", "sustainable"],
                            "price": 42.99,
                            "average_rating": 4.8
                        },
                        {
                            "product_id": "223e4567-e89b-12d3-a456-426614174001",
                            "name": "Hand-knitted Wool Scarf",
                            "description": "Warm and cozy scarf made from ethically sourced merino wool.",
                            "handcrafter_name": "Alex Weaver",
                            "categories": ["clothing", "accessories", "winter"],
                            "price": 35.50,
                            "average_rating": 4.9
                        }
                    ]
                }
            }

class StoreProductResponse(BaseModel):
    products_stored: int = Field(...,description="Number of products successfully stored",examples=[3])
    message: str = Field(
        ..., 
        description="Status message about the storage operation",
        examples=["Products Stored Successfully"])
    
    class Config:
        schema_extra = {
            "example": {
                "products_stored": 2,
                "message": "Products Stored Successfully"
            }
        }


class RecommendProductRequest(BaseModel):
    history: List[str] = Field(
        ...,
        description="List of product IDs the user has viewed or purchased",
        examples=[["123e4567-e89b-12d3-a456-426614174000", "223e4567-e89b-12d3-a456-426614174001"]])
    top_k: int = Field(
        default=3,
        description="Number of recommendations to return",
        examples=[3],
        ge=1,
        le=20
    )


class ProductRecommendation(BaseModel):
    id: str = Field(
        ...,
        description="Unique identifier of the recommended product",
        examples=["323e4567-e89b-12d3-a456-426614174002"]
    )
    name: str = Field(
        ...,
        description="Name of the recommended product",
        examples=["Ceramic Coffee Mug"]
    )
    score: float = Field(
        ...,
        description="Similarity score (higher means more relevant)",
        examples=[0.92]
    )
    
    class Config:
        schema_extra = {
            "example": {
                "id": "323e4567-e89b-12d3-a456-426614174002",
                "name": "Ceramic Coffee Mug",
                "score": 0.92
            }
        }

class RecommendProductResponse(BaseModel):
    products: List[ProductRecommendation] = Field( ...,description="List of recommended products")
    
    class Config:
        schema_extra = {
            "example": {
                "products": [
                    {
                        "id": "323e4567-e89b-12d3-a456-426614174002",
                        "name": "Ceramic Coffee Mug",
                        "score": 0.92
                    },
                    {
                        "id": "423e4567-e89b-12d3-a456-426614174003",
                        "name": "Handmade Cutting Board",
                        "score": 0.87
                    },
                    {
                        "id": "523e4567-e89b-12d3-a456-426614174004",
                        "name": "Wooden Salad Servers",
                        "score": 0.81
                    }
                ]
            }
        }
