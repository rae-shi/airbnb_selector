from client import collection
from llm_extractor import extract_filters_from_query
from utils.embedding_utils import get_embedding
from search.exact_search import run_exact_search
from search.geo_search import run_geo_search
from search.vector_search import run_vector_search
from search.result_utils import deduplicate_and_rank
from utils.dynamic_parser import DynamicParser
from utils.formatting import pretty_print_listing
import requests

def geocode_location(location_str):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": location_str,
        "format": "json",
        "limit": 1
    }
    response = requests.get(url, params=params, headers={"User-Agent": "airbnb-selector-app"})
    data = response.json()
    if data:
        lat = float(data[0]["lat"])
        lon = float(data[0]["lon"])
        return {"longitude": lon, "latitude": lat, "radius": 2000}
    return None

use_input = input("Enter your query: ")
user_query = use_input.lower()

dynamic_parser = DynamicParser()
valid_fields = dynamic_parser.all_fields.keys()

filters = extract_filters_from_query(user_query)

exact_filters = {k: v for k, v in filters.get("exact_filters", {}).items() if k in valid_fields}
exact_results = run_exact_search(collection, exact_filters)

location_str = filters.get("location_filters")
print(f'the location str: ${location_str}')
location_dict = geocode_location(location_str)
geo_results = run_geo_search(collection, location_dict)

if filters.get("semantic_filters"):
    query_embedding = get_embedding(user_query)
    semantic_filters = filters.get("semantic_filters")
    if isinstance(semantic_filters, dict):
        vector_results = run_vector_search(collection, query_embedding, semantic_filters)
    else:
        vector_results = run_vector_search(collection, query_embedding, None)
else:
    vector_results = []

final_results = deduplicate_and_rank(exact_results, geo_results, vector_results)

for i, doc in enumerate(final_results, 1):
    print(f"Listing {i}:")
    pretty_print_listing(doc)

