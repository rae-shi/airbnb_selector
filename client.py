from pymongo import MongoClient
import os
from dotenv import load_dotenv
from openai import OpenAI
import httpx

# Load environment variables from .env file
# This allows us to store sensitive information like database credentials securely
load_dotenv()

http_client = httpx.Client(trust_env=False)

# Establish connection to MongoDB Atlas using only the connection string
client = MongoClient(os.getenv('MONGODB_URI'))
db = client['sample_airbnb']  # Connect to the sample_airbnb database
collection = db['listingsAndReviews']  # Access the listingsAndReviews collection

# openai client
openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'), http_client=http_client)