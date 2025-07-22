def run_exact_search(collection, exact_filters):
    if not exact_filters:
        return []
    print("exact_filters", exact_filters)
    return list(collection.find(exact_filters).limit(5))
  
  # how to run the exact search itself to search in the mongo db
