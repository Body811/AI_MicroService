# from decouple import Config, RepositoryEnv
import os

class Settings:
    APP_NAME = os.getenv("APP_NAME", "AI Microservice")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true" 
    QDRANT_URL = os.getenv("QDRANT_URL")
    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
    QDRANT_SIMILARITY_COLLECTION_NAME = os.getenv("QDRANT_SIMILARITY_COLLECTION_NAME", "Similarity_Search")
    QDRANT_SIMILARITY_COLLECTION_VECTOR_SIZE = int(os.getenv("QDRANT_SIMILARITY_COLLECTION_VECTOR_SIZE", "1000"))
    QDRANT_RECOMMENDATION_COLLECTION_NAME = os.getenv("QDRANT_RECOMMENDATION_COLLECTION_NAME", "Product_Recommendation")
    QDRANT_RECOMMENDATION_COLLECTION_VECTOR_SIZE = int(os.getenv("QDRANT_RECOMMENDATION_COLLECTION_VECTOR_SIZE", "386"))

settings = Settings()


# config = Config(RepositoryEnv(".env"))
# class Settings:
    
#     APP_NAME = config("APP_NAME", default="AI Microservice")
#     DEBUG = config("DEBUG", default=False, cast=bool)
#     QDRANT_URL = config("QDRANT_URL")
#     QDRANT_API_KEY = config("QDRANT_API_KEY")
#     QDRANT_SIMILARITY_COLLECTION_NAME = config("QDRANT_SIMILARITY_COLLECTION_NAME")
#     QDRANT_SIMILARITY_COLLECTION_VECTOR_SIZE=config("QDRANT_SIMILARITY_COLLECTION_VECTOR_SIZE")
#     QDRANT_RECOMMENDATION_COLLECTION_NAME = config("QDRANT_RECOMMENDATION_COLLECTION_NAME")
#     QDRANT_RECOMMENDATION_COLLECTION_VECTOR_SIZE=config("QDRANT_RECOMMENDATION_COLLECTION_VECTOR_SIZE")
    
# settings = Settings()

