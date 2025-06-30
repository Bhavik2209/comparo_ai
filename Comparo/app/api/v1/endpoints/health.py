from fastapi import APIRouter


router = APIRouter()

@router.get("/")
async def health_check():
    """
    Health check endpoint to verify the service is running.
    """
    return {"status": "ok", "message": "Service is running"}