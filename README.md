# Airbnb Selector

Airbnb Selector is a tool that helps you find the best Airbnb listings for your needs, using natural language search and smart filtering. Just describe what you want, and the app will search a MongoDB Airbnb dataset and recommend listings that fit your preferences.

---

## Features
- **Search in plain English:** Type what you’re looking for, like "affordable apartment near Central Park with great reviews."
- **Smart filter extraction:** The app figures out what you care about (like price, location, amenities) and builds the right search.
- **Combines multiple search types:** It uses exact filters, location-based search, and semantic (meaning-based) search to find the best matches.
- **Flexible to data changes:** The app automatically adapts if the Airbnb dataset changes.
- **Friendly recommendations:** After searching, it summarizes the top listings and gives you a clear, helpful recommendation.

---

## Getting Started

1. **Clone this repository:**
   ```bash
   git clone <your-repo-url>
   cd airbnb-selector
   ```

2. **Install the requirements:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your environment variables:**
   Create a `.env` file in the project root with your MongoDB and OpenAI keys:
   ```
   MONGODB_URI=your_mongodb_connection_string
   OPENAI_API_KEY=your_openai_api_key
   ```

4. **(Optional) Generate embeddings:**
   If you haven’t already, run the embedding utility to add vector embeddings to your listings for better search results.

---

## How to Use

1. **Start the app:**
   ```bash
   python main.py
   ```
2. **Enter your search:**
   For example: `"Looking for a cozy, cheap apartment in Toronto near the CN Tower"`
3. **See your results:**
   The app will show you the top listings and a recommendation based on your search.

---

## Project Structure

```
.
├── main.py                # Main script
├── client.py              # Database and OpenAI client setup
├── config.py              # App configuration
├── llm_extractor.py       # Extracts filters from user queries
├── search/                # Search modules (exact, geo, vector, result utils)
├── utils/                 # Utilities (embedding, formatting, dynamic parser)
├── requirements.txt       # Python dependencies
├── .env.example           # Example environment file
└── README.md              # This file
```

---

## Contributing
If you have ideas or find bugs, feel free to open an issue or pull request.

---

## License
MIT License. See [LICENSE](LICENSE) for details. 