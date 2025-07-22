from collections import defaultdict
from client import collection

class DynamicParser:
    """
    A parser that dynamically discovers database fields and extracts user preferences
    from natural language prompts.
    """
    
    def __init__(self):
        """
        Initialize the parser by discovering all available fields in the database.
        This ensures we don't need to hardcode field names and can adapt to schema changes.
        """
        self.all_fields = {}  # Dictionary to store field names and their data types
        self.discover_fields()  # Automatically discover fields from the database
    
    def discover_fields(self):
        """
        Dynamically discover all fields and their data types from the MongoDB collection.
        This method samples documents from the database to understand the schema structure.
        """
        # Get a sample of 100 documents to analyze the structure
        # Using a sample is more efficient than analyzing all documents
        sample_docs = list(collection.find().limit(100))
        
        # Use defaultdict to automatically create empty sets for new fields
        field_types = defaultdict(set)
        
        # Analyze each document to collect all field names and their types
        for doc in sample_docs:
            for key, value in doc.items():
                field_types[key].add(type(value))
        
        # Determine the most common type for each field
        for field, types in field_types.items():
            # Remove None type if other types exist (None usually means missing data)
            if len(types) > 1 and type(None) in types:
                types.remove(type(None))
            
            # Choose the most appropriate type based on priority
            # Priority: int > float > str > list > dict > bool > None
            if int in types:
                self.all_fields[field] = int
            elif float in types:
                self.all_fields[field] = float
            elif str in types:
                self.all_fields[field] = str
            elif list in types:
                self.all_fields[field] = list
            elif dict in types:
                self.all_fields[field] = dict
            elif bool in types:
                self.all_fields[field] = bool
            else:
                self.all_fields[field] = type(None)
