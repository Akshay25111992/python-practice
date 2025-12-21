# FastAPI Application - Login Management System
# 
# Setup Instructions:
# 1. Install dependencies: pip install -r requirements.txt
# 2. Update database credentials in config.py
# 3. Create the database in PostgreSQL/MySQL
# 4. Run the application: uvicorn main:app --reload
# 5. Access API docs at: http://127.0.0.1:8000/docs

from fastapi import FastAPI
from database import engine, Base
from routes import router

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI application
app = FastAPI(
    title="Login Management API",
    description="A FastAPI application with user registration and login functionality",
    version="1.0.0"
)

# Include authentication routes
app.include_router(router, tags=["Authentication"])


@app.get("/", tags=["Root"])
def read_root():
    """Root endpoint - Welcome message."""
    return {
        "message": "Welcome to the Login Management API",
        "docs": "/docs",
        "endpoints": {
            "register": "POST /register",
            "login": "POST /login",
            "me": "GET /me (protected)"
        }
    }


# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

