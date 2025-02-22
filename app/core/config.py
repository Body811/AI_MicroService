from decouple import Config, RepositoryEnv


config = Config(RepositoryEnv("app\.env"))
class Settings:
    
    APP_NAME = config("APP_NAME", default="AI Microservice")
    DEBUG = config("DEBUG", default=False, cast=bool)
    QDRANT_URL = config("QDRANT_URL")
    QDRANT_API_KEY = config("QDRANT_API_KEY")
    QDRANT_SIMILARITY_COLLECTION_NAME = config("QDRANT_SIMILARITY_COLLECTION_NAME")
    QDRANT_SIMILARITY_COLLECTION_VECTOR_SIZE=config("QDRANT_SIMILARITY_COLLECTION_VECTOR_SIZE")
    
    
settings = Settings()