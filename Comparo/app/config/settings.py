# app/config/settings.py

from pydantic_settings import BaseSettings
from typing import Optional, List
from pathlib import Path
import os

class Settings(BaseSettings):
    """
    Application settings with environment variable support
    """
    
    # ========== API KEYS ==========
    GROQ_API_KEY: str
    TAVILY_API_KEY: str
    YOUTUBE_API_KEY: str  # Also called KEY in your original code
    GOOGLE_API_KEY: str
    NEWS_API_KEY: Optional[str] = None  # Optional, can be used for news-related features
    
   
# Create global settings instance
settings = Settings()

