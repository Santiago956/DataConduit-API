from fastapi.responses import RedirectResponse
from src.app import app


@app.get("/")
def home():
    return RedirectResponse("/docs")