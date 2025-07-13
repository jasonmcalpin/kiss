from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from .config import HOST, PORT, DEBUG
from .database import db

app = FastAPI(
    title="KISS API",
    description="Gameplay API",
    version="0.1.0",
    debug=DEBUG
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    """Root endpoint"""
    return {"message": "KISS Game API", "status": "running"}

@app.get("/health")
def health_check():
    """Health check endpoint"""
    try:
        result = db.execute_query("SELECT 1 as test")
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": "disconnected", "error": str(e)}

@app.get("/api/universe")
def get_universe():
    """Get universe data (placeholder for 32x32 grid)"""
    # TODO: Implement universe generation
    return {
        "universe": {
            "size": "32x32",
            "systems": [],
            "message": "Map display"
        }
    }

@app.post("/api/universe/generate")
def generate_universe():
    """Generate universe data (placeholder for 32x32 grid)"""
    # TODO: Implement universe generation
    return {
        "universe": {
            "size": "32x32",
            "systems": [],
            "message": "Map display"
        }
    }

@app.post("/api/universe/update")
def update_universe():
    """Update universe data (placeholder for 32x32 grid)"""
    # TODO: Implement universe update
    return {
        "universe": {
            "size": "32x32",
            "systems": [],
            "message": "Map display"
        }
    }

@app.get("/api/game/status")
def get_game_status():
    """Get current game status"""
    return {
        "game": {
            "active": False,
            "players": 0,
            "turn": 0,
            "message": "Game logic coming soon!"
        }
    }

@app.post("/api/empire/create")
def create_empire(empire_data: dict):
    """Create a new empire (placeholder)"""
    # TODO: Implement empire creation
    return {
        "success": True,
        "empire": {
            "name": empire_data.get("name", "Unknown Empire"),
            "special_ability": empire_data.get("special_ability", "none"),
            "message": "Empire creation coming soon!"
        }
    }

@app.post("/api/empire/update")
def update_empire(empire_data: dict):
    """Update an existing empire (placeholder)"""
    # TODO: Implement empire update
    return {
        "success": True,
        "empire": {
            "name": empire_data.get("name", "Unknown Empire"),
            "special_ability": empire_data.get("special_ability", "none"),
            "message": "Empire creation coming soon!"
        }
    }

if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT, reload=DEBUG)
