import os
from openai import OpenAI
from dotenv import load_dotenv
from pymongo import MongoClient
from tqdm import tqdm
import httpx

load_dotenv()

http_client = httpx.Client(trust_env=False)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), http_client=http_client)

# MongoDB connection
mongo_client = MongoClient(os.getenv('MONGODB_URI'))
db = mongo_client['sample_airbnb']
collection = db['listingsAndReviews']

# Embedding model and dimension
EMBEDDING_MODEL = "text-embedding-3-small"


def get_embedding(text, model=EMBEDDING_MODEL):
    """
    Generate an embedding for the given text using OpenAI.
    """
    response = client.embeddings.create(
        input=text,
        model=model
    )
    return response.data[0].embedding


def update_listings_with_embeddings():
    """
    Update all listings in the collection with an embedding if not already present.
    """
    for doc in tqdm(collection.find({"embedding": {"$exists": False}})):
        # Gather all relevant fields
        fields = [
            doc.get("name", ""),
            doc.get("summary", ""),
            doc.get("space", ""),
            doc.get("description", ""),
            doc.get("neighborhood_overview", ""),
            doc.get("notes", ""),
            doc.get("transit", ""),
            doc.get("access", ""),
            doc.get("interaction", ""),
            doc.get("house_rules", "")
        ]
        # Add all review comments
        if "reviews" in doc and isinstance(doc["reviews"], list):
            first_5_reviews = doc["reviews"][:5] if len(doc["reviews"]) > 5 else doc["reviews"]
            review_comments = [
                review.get("comments", "") for review in first_5_reviews if "comments" in review
            ]
            fields.extend(review_comments)
        # Combine all text
        text = " ".join(fields).strip()
        if text:
            embedding = get_embedding(text)
            collection.update_one(
                {"_id": doc["_id"]},
                {"$set": {"embedding": embedding}}
            )

