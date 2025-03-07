import requests
from PIL import Image
from io import BytesIO
import aiohttp
import asyncio
from app.core.image_utils import preprocess_image, get_image_embedding, download_image
from qdrant_client import models
from app.core.config import settings
from app.core.qdrant_utils import qdrant_client
import io
 
#TODO service to get closest item: (1 url) -> returns list of product ids
#TODO service to delete an item: (id:int) -> returns message

async def store_image_service(image_data):
    keys = list(image_data.keys())  



    async with aiohttp.ClientSession() as session:
        tasks = [download_image(session, url) for url in image_data.values()]
        image_list = await asyncio.gather(*tasks)


    inputs = preprocess_image(images=image_list)
    embeddings = get_image_embedding(inputs=inputs)


    points = [
        models.PointStruct(
            id=keys[idx],  
            vector=embeddings[idx],  
            payload={"url": image_data[keys[idx]]}  
        )
        for idx in range(len(keys))
    ]
    
        
    qdrant_client.upload_points(
        collection_name=settings.QDRANT_SIMILARITY_COLLECTION_NAME,
        points=points
    )
    
    return len(keys)


async def search_image_service(file, top_k):
    
    image_bytes = await file.read()
    
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    
    inputs = preprocess_image(images=image)
    embeddings = get_image_embedding(inputs=inputs)

    results = qdrant_client.query_points(
        collection_name=settings.QDRANT_SIMILARITY_COLLECTION_NAME,
        query=embeddings[0].tolist(),
        limit=top_k
    )
    
    search_result = [
        {
            "id": str(result.id),
            "url": result.payload["url"],
            "score": result.score
        }
        for result in results.points
    ]

    return search_result
    
def delete_image_service(ids):
    
    qdrant_client.delete(
        collection_name=settings.QDRANT_SIMILARITY_COLLECTION_NAME,
        points_selector=ids
    )
    