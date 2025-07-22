def run_vector_search(collection, query_embedding, filter_dict=None):
    vector_query = {
        "$vectorSearch": {
            "exact": False,
            "index": "vector_index",
            "limit": 5,
            "numCandidates": 1000,
            "path": "embedding",
            "queryVector": query_embedding
        }
    }
    if filter_dict:
        vector_query["$vectorSearch"]["filter"] = filter_dict
    print("vector_query", vector_query)
    return list(collection.aggregate([vector_query]))