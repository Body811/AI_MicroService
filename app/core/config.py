# from decouple import Config, RepositoryEnv
import os

class Settings:
    APP_NAME = os.getenv("APP_NAME", "AI Microservice")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"  # Convert string to bool
    
    # Qdrant Settings
    QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY", "")
    QDRANT_SIMILARITY_COLLECTION_NAME = os.getenv("QDRANT_SIMILARITY_COLLECTION_NAME", "similarity_collection")
    QDRANT_SIMILARITY_COLLECTION_VECTOR_SIZE = int(os.getenv("QDRANT_SIMILARITY_COLLECTION_VECTOR_SIZE", "512"))
    QDRANT_RECOMMENDATION_COLLECTION_NAME = os.getenv("QDRANT_RECOMMENDATION_COLLECTION_NAME", "recommendation_collection")
    QDRANT_RECOMMENDATION_COLLECTION_VECTOR_SIZE = int(os.getenv("QDRANT_RECOMMENDATION_COLLECTION_VECTOR_SIZE", "512"))

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

