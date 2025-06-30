# Comparo AI

Comparo AI is an **agentic AI project** designed for advanced smartphone comparisons. It leverages LLMs, web search, and structured data extraction to provide detailed, dynamic, and user-friendly smartphone comparison reports. The project features a FastAPI backend and a modern Chainlit-based frontend for interactive user experience.

---

## Features
- **Agentic AI workflow** for multi-step information gathering and reasoning
- **Smartphone comparison** with specs, pros/cons, reviews, and best product recommendation
- **Web search and content extraction** for up-to-date information
- **YouTube video suggestions** for the best product
- **Modern Chainlit frontend** with card-based UI
- **Extensible and modular codebase**

---

## Project Structure
```
Comparo/
  app/                # FastAPI backend application
    api/              # API endpoints and routers
    config/           # Configuration and settings
    core/             # Agentic workflow and nodes
    models/           # Pydantic models for requests/responses
    services/         # LLM, web, and content services
    utils/            # Utility functions and exceptions
    main.py           # FastAPI app entrypoint
  tests/              # Unit and integration tests
  requirements.txt    # Python dependencies
  README.md           # Project documentation (this file)
  Dockerfile          # (Optional) Docker support
```

---

## Requirements
- Python 3.9+
- [Chainlit](https://docs.chainlit.io/) (for frontend)
- [FastAPI](https://fastapi.tiangolo.com/), [httpx], [uvicorn], and other dependencies (see `requirements.txt`)

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Running the FastAPI Backend (API)
1. **Navigate to the Comparo directory:**
   ```bash
   cd Comparo
   ```
2. **Start the FastAPI server:**
   ```bash
   uvicorn app.main:app --reload
   ```
   The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Running the Chainlit Frontend
1. **Go to the project root (where `frontend.py` is located):**
   ```bash
   cd ..  # If you are inside Comparo, go up one level
   ```
2. **Start Chainlit:**
   ```bash
   chainlit run frontend.py
   ```
   This will launch the Chainlit UI in your browser.

---

## Example Usage
- Enter a query like:
  > Best smartphone under 30000 India 2025 for best camera quality
- The frontend will display cards for each product, highlight the best product, and show a YouTube review link if available.

---

## About
- **Project Name:** Comparo AI
- **Purpose:** Agentic AI for smartphone comparisons
- **Tech:** FastAPI, Chainlit, LLMs, web search, Python
- **Author:** Bhavik Rohit

---

## License
This project is licensed under the MIT License.

---

## Contact
For questions, suggestions, or contributions, please open an issue or contact the maintainer.
