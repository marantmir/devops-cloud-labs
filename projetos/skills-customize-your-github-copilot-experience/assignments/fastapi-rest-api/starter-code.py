"""
FastAPI REST API Starter Code
Build a complete REST API using FastAPI framework
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

# Initialize FastAPI application
app = FastAPI(
    title="Todo API",
    description="A simple Todo management API built with FastAPI",
    version="1.0.0"
)

# Define Pydantic models for data validation
class TodoItem(BaseModel):
    """Model for a Todo item"""
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    completed: bool = False

class TodoUpdate(BaseModel):
    """Model for updating a Todo item"""
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

# In-memory database (replace with real database in production)
todos_db: dict[int, TodoItem] = {}
next_id = 1

# TODO: Implement your endpoints here
# 1. GET /todos - Get all todos with optional filtering
# 2. GET /todos/{todo_id} - Get a specific todo by ID
# 3. POST /todos - Create a new todo
# 4. PUT /todos/{todo_id} - Update a specific todo
# 5. DELETE /todos/{todo_id} - Delete a specific todo

@app.get("/")
async def read_root():
    """Root endpoint - verify API is running"""
    return {"message": "Welcome to Todo API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
