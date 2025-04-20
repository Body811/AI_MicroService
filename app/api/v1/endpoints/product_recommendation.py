from fastapi import APIRouter, HTTPException
from app.services.product_recommendation_service import store_product_service, recommend_product_service
from app.api.v1.models.product_recommendation import *

router = APIRouter()


@router.post("/store", response_model=StoreProductResponse)
async def store_product(request: StoreProductRequest):
    try:
        stored_products = await store_product_service(request.products)   
        return StoreProductResponse(
            products_stored = stored_products,
            message="Products Stored Successfully"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




@router.post("/recommend",response_model=RecommendProductResponse)
async def recommend_product(request: RecommendProductRequest):
    try:
        results = await recommend_product_service(request.history,request.top_k)
        return RecommendProductResponse(products=results)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



# @router.delete("/delete",response_model=DeleteproductResponse)
# async def delete_product(request: DeleteproductRequest):
#     try:
        
#         delete_product_service(request.ids)
#         return DeleteproductResponse(
#             message=f"Deleted {len(request.ids)} items successfully"
#         )
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
 