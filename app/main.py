from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.services.country_service import country_service
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# Add CORS Middleware to allow Next.js frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://surajkumar.space",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"message": "Welcome to the Country Capital API"}

@app.get("/capital")
async def get_capital(country: str):
    if not country:
        raise HTTPException(status_code=400, detail="Country name is required")
    
    try:
        capital = country_service.get_capital(country)
        return {"country": country, "capital": capital}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
