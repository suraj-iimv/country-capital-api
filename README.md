# Country Capital Finder API

A modular backend API for finding country capitals, refactored from a Streamlit monolith.

## Structure

- `app/`: Core application logic.
  - `core/`: Configuration and settings.
  - `services/`: Business logic and external integrations (OpenRouter).
  - `main.py`: FastAPI entry point.
- `streamlit_app.py`: Legacy Streamlit UI, now using the service layer.
- `requirements.txt`: Project dependencies.
- `.env.example`: Template for environment variables.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure environment variables:
   - Copy `.env.example` to `.env`
   - Add your `OPENROUTER_API_KEY` to `.env`

## Running the API

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.
Documentation: `http://localhost:8000/docs`

## Running the Streamlit UI

```bash
streamlit run streamlit_app.py
```
