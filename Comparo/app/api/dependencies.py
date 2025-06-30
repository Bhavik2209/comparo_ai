# app/api/dependencies.py

from fastapi import Depends, HTTPException
from app.config.settings import settings
from typing import Dict, Any
import os

async def get_workflow_dependencies() -> Dict[str, Any]:
    """
    Dependency to validate API keys and return workflow dependencies
    """
    # Validate required API keys
    required_keys = {
        "GROQ_API_KEY": settings.GROQ_API_KEY,
        "TAVILY_API_KEY": settings.TAVILY_API_KEY, 
        "YOUTUBE_API_KEY": settings.YOUTUBE_API_KEY,
        "GOOGLE_API_KEY": settings.GOOGLE_API_KEY
    }
    
    missing_keys = []
    for key_name, key_value in required_keys.items():
        if not key_value or key_value.strip() == "":
            missing_keys.append(key_name)
    
    if missing_keys:
        raise HTTPException(
            status_code=500,
            detail=f"Missing required API keys: {', '.join(missing_keys)}"
        )
    
    return {
        "api_keys_validated": True,
        "groq_api_key": settings.GROQ_API_KEY,
        "tavily_api_key": settings.TAVILY_API_KEY,
        "youtube_api_key": settings.YOUTUBE_API_KEY,
        "google_api_key": settings.GOOGLE_API_KEY
    }

def validate_request_data(query: str) -> str:
    """
    Validate and sanitize request data
    """
    if not query or query.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Query parameter cannot be empty"
        )
    
    # Basic sanitization
    query = query.strip()
    
    # Length validation
    if len(query) > 500:
        raise HTTPException(
            status_code=400,
            detail="Query too long. Maximum 500 characters allowed."
        )
    
    return query