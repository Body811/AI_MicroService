from qdrant_client import models  
from core.config import settings
from core.qdrant_utils import qdrant_client
from core.recommendation_utils import process_product_data
from api.v1.models.product_recommendation import ProductRecommendation
from qdrant_client.models import PointStruct
import numpy as np


async def store_product_service(products):

    text_embeddings, numerical_features = process_product_data(products)
    
    points = []
    
    for i, product in enumerate(products):
        vector = np.concatenate([text_embeddings[i], numerical_features[i]])  
       
        point = PointStruct(
            id=product.product_id,  
            vector=vector.tolist(),
            payload={"name": product.name}  
        )
        points.append(point)
    qdrant_client.upsert(collection_name=settings.QDRANT_RECOMMENDATION_COLLECTION_NAME, points=points)
    
    return len(points)

async def recommend_product_service(history_ids, top_k):
    
    if not history_ids:
        raise Exception("History IDs list is empty")
    
    query_result = qdrant_client.retrieve(
    collection_name=settings.QDRANT_RECOMMENDATION_COLLECTION_NAME,
    ids=history_ids,
    with_vectors=True  
    )

    if not query_result:
        raise ValueError("None of the product IDs in history were found")
    
    history_vectors = []
    found_ids = []
    
    for record in query_result:
        if record.vector:  # Check if vector exists
            history_vectors.append(record.vector)
            found_ids.append(str(record.id))  

    if not history_vectors:
        raise ValueError("No vectors found for the given product IDs")

    composite_vector = np.mean(history_vectors, axis=0)
    
    raw_results = qdrant_client.search(
        collection_name=settings.QDRANT_RECOMMENDATION_COLLECTION_NAME,
        query_vector=composite_vector.tolist(), 
        limit=top_k + len(history_ids), 
        query_filter=models.Filter(  

        )
    )
    
    results = [
        r for r in raw_results 
            if str(r.id) not in {str(id) for id in history_ids}
        ][:top_k]
    
    search_result = [
        ProductRecommendation(
            id=str(result.id),  
            name=result.payload.get("name"),  
            score=float(result.score)  
        )
        for result in results
    ]
    
    return search_result   




