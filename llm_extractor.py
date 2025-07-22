import json
from config import MODEL_CONFIG
from client import openai_client as client

def extract_filters_from_query(user_query: str) -> dict:
    """
    Uses an LLM to extract structured filters from a natural language user query.

    Args:
        user_query (str): The raw query from the user.

    Returns:
        dict: A dictionary containing 'exact_filters', 'location_filters', 
              and 'semantic_filters'. Returns an empty dict on failure.
    """
    if not client:
        print("OpenAI client not initialized. Cannot extract filters.")
        return {}

    # This is the system prompt that instructs the LLM on how to behave.
    # We are asking it to act as an API that returns a JSON object.
    system_prompt = """
    You are an intelligent travel assistant API. Your job is to analyze a user's query and extract key information into a structured JSON format.

    The user will provide a prompt about their desired travel accommodation. You must identify and separate the criteria into three categories:
    1.  `exact_filters`: These are concrete, non-negotiable requirements that can be directly mapped to database fields. Examples include number of bedrooms, specific amenities (e.g., "pool", "wifi", "kitchen"), or a price range.
    2.  `location_filters`: This should only contain specific geographic information mentioned by the user, such as a city, neighborhood, or address.
    3.  `semantic_filters`: These are subjective, vague, or qualitative descriptions that require semantic understanding. Examples include "a cozy vibe", "a place with a great view", "family-friendly", or "good for a romantic getaway".

    Your response must be a valid JSON object with the keys "exact_filters", "location_filters", and "semantic_filters". Do not include any other text or explanations in your response.
    - For `exact_filters`, the value should be a dictionary.
    - For `location_filters`, the value should be a string.
    - For `semantic_filters`, the value should be a string containing the vague terms.
    If a category is not mentioned in the user's query, return an empty value for that key (e.g., {} or "").
    """

    try:
        completion = client.chat.completions.create(
            model=MODEL_CONFIG["llm"]["model"],
            response_format={"type": "json_object"},  # Enable JSON mode
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query}
            ],
            temperature=MODEL_CONFIG["llm"]["temperature"],
        )
        
        response_content = completion.choices[0].message.content
        extracted_data = json.loads(response_content)
        
        return extracted_data

    except Exception as e:
        print(f"An error occurred while calling the OpenAI API: {e}")
        return {}
