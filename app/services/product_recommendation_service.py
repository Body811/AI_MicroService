from qdrant_client import models  
from core.config import settings
from core.qdrant_utils import qdrant_client
from core.recommendation_utils import process_product_data
from api.v1.models.product_recommendation import ProductRecommendation
from qdrant_client.models import PointStruct
from datetime import datetime
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

async def recommend_product_service(history_items, top_k):
    
    if not history_items:
        raise Exception("History items list is empty")
    
    history_ids = [item.id for item in history_items]
    
    query_result = qdrant_client.retrieve(
    collection_name=settings.QDRANT_RECOMMENDATION_COLLECTION_NAME,
    ids=history_ids,
    with_vectors=True  
    )

    if not query_result:
        raise ValueError("None of the product IDs in history were found")
    
    
    history_lookup = {item.id: item for item in history_items}
    
    history_vectors = []
    weights = []
    found_ids = []
    
    today = datetime.now().date()
    
    for record in query_result:
        if record.vector:  
            found_ids.append(str(record.id))  
            history_item = history_lookup.get(str(record.id))
            if history_item:
                history_vectors.append(record.vector)
                days_ago = (today - datetime.strptime(history_item.date, "%Y-%m-%d").date()).days
                recency_weight = 1.0 / (1.0 + days_ago)  
                combined_weight = recency_weight * (1.0 + 0.2 * history_item.view_count)
                weights.append(combined_weight) 
            else:
                weights.append(1.0)

    if not history_vectors:
        raise ValueError("No vectors found for the given product IDs")


    weights = np.array(weights)
    weights = weights / np.sum(weights)

    composite_vector = np.average(history_vectors, axis=0, weights=weights)

    raw_results = qdrant_client.search(
        collection_name=settings.QDRANT_RECOMMENDATION_COLLECTION_NAME,
        query_vector=composite_vector.tolist(), 
        limit=top_k + len(found_ids),
        with_payload=True,
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




