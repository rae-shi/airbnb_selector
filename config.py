from enum import Enum

# OpenAI Models
class OpenAIModels(Enum):
    GPT4 = "gpt-4-turbo-preview"  # Most capable model, but more expensive
    GPT35 = "gpt-3.5-turbo"       # Good balance of capability and cost
    
# OpenAI Embedding Models
class EmbeddingModels(Enum):
    DEFAULT = "text-embedding-3-small"     # Cheaper, good for most use cases
    LARGE = "text-embedding-3-large"       # More expensive, better quality

# Model Configuration
MODEL_CONFIG = {
    # LLM Settings
    "llm": {
        "model": OpenAIModels.GPT35.value,  # Default to GPT-3.5 for cost efficiency
        "temperature": 0.7,                  # Higher = more creative, Lower = more focused
        "max_tokens": 500,                   # Maximum length of response
    },
    
    # Embedding Settings
    "embeddings": {
        "model": EmbeddingModels.DEFAULT.value,
        "dimensions": 1536,                  # Dimension of embedding vectors
    },
    
    # Vector Search Settings
    "vector_search": {
        "index_name": "default",            # Name of the vector search index in MongoDB
        "num_candidates": 100,              # Number of candidates to consider
        "num_results": 10,                  # Number of results to return
    },
    
    # Geo Search Settings
    "geo_search": {
        "default_radius_km": 5,             # Default search radius in kilometers
        "max_radius_km": 50,               # Maximum allowed search radius
    }
}

# MongoDB Collection Names
COLLECTIONS = {
    "listings": "listingsAndReviews",
    "embeddings": "listingEmbeddings",      # Collection to store pre-computed embeddings
}

# Query Processing Settings
QUERY_PROCESSING = {
    "min_confidence_score": 0.7,            # Minimum confidence score for extracted filters
    "max_price_multiplier": 1.5,            # Price range flexibility
    "default_limit": 10,                    # Default number of results to return
}

# Cache Settings
CACHE_CONFIG = {
    "enable_cache": True,                   # Whether to cache results
    "cache_expiry": 3600,                  # Cache expiry time in seconds (1 hour)
}

# API Rate Limiting
RATE_LIMITS = {
    "openai_rpm": 60,                      # Requests per minute for OpenAI
    "mongodb_ops_sec": 1000,               # MongoDB operations per second
} 