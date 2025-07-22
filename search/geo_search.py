def run_geo_search(collection, location_dict):
    if not location_dict:
        return []
    try:
        geo_query = {
            "address.location": {
                "$near": {
                    "$geometry": {
                        "type": "Point",
                        "coordinates": [location_dict["longitude"], location_dict["latitude"]]
                    },
                    "$maxDistance": location_dict.get("max_distance", 50000)
                }
            }
        }
        print("geo_query", geo_query)
        return list(collection.find(geo_query).limit(5))
    except Exception as e:
        print(f"Geo search error: {e}")
        return []
    
