#!/usr/bin/env python3
"""
FastAPI Project Structure Generator
Creates the complete directory and file structure for smartphone comparison API
"""

import os
from pathlib import Path

def create_file_structure():
    """Create the complete FastAPI project structure with empty files"""
    
    # Base project directory
    base_dir = Path("Comparo")
    
    # All files and directories to create
    files_and_dirs = [
        # Root level files
        "requirements.txt",
        ".env.example", 
        ".env",
        ".gitignore",
        "README.md",
        "Dockerfile",
        
        # App directory structure
        "app/__init__.py",
        "app/main.py",
        
        # Config
        "app/config/__init__.py",
        "app/config/settings.py",
        
        # Models
        "app/models/__init__.py",
        "app/models/request_models.py",
        "app/models/response_models.py", 
        "app/models/schema_models.py",
        
        # Services
        "app/services/__init__.py",
        "app/services/tavily_service.py",
        "app/services/llm_service.py",
        "app/services/youtube_service.py",
        "app/services/content_loader.py",
        
        # Core
        "app/core/__init__.py",
        "app/core/graph_workflow.py",
        "app/core/nodes.py",
        
        # API
        "app/api/__init__.py",
        "app/api/v1/__init__.py",
        "app/api/v1/router.py",
        "app/api/v1/endpoints/__init__.py",
        "app/api/v1/endpoints/comparison.py",
        "app/api/v1/endpoints/health.py",
        "app/api/dependencies.py",
        
        # Utils
        "app/utils/__init__.py",
        "app/utils/exceptions.py",
        "app/utils/helpers.py",
        
        # Tests
        "tests/__init__.py",
        "tests/test_main.py",
        "tests/test_services/__init__.py",
        "tests/test_services/test_tavily_service.py",
        "tests/test_services/test_llm_service.py", 
        "tests/test_api/__init__.py",
        "tests/test_api/test_comparison.py"
    ]
    
    print(f"Creating project structure in: {base_dir}")
    print("=" * 50)
    
    # Create base directory
    base_dir.mkdir(exist_ok=True)
    
    # Create all files and directories
    for file_path in files_and_dirs:
        full_path = base_dir / file_path
        
        # Create parent directories if they don't exist
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Create empty file
        full_path.touch()
        print(f"Created: {full_path}")
    
    print("=" * 50)
    print(f"✅ Project structure created successfully!")
    print(f"📁 Base directory: {base_dir.absolute()}")
    print(f"📄 Total files created: {len(files_and_dirs)}")
    print("\nNext steps:")
    print("1. Navigate to the project directory")
    print("2. Add your API keys to .env file")
    print("3. Install dependencies: pip install -r requirements.txt")
    print("4. Start coding your FastAPI application!")

if __name__ == "__main__":
    create_file_structure()