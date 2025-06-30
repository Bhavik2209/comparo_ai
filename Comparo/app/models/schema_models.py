from typing import Optional, Dict, TypedDict, List
from pydantic import BaseModel, Field

class SmartphoneReview(BaseModel):
    """A review of a smartphone."""
    title: str = Field(..., description="The title of the smartphone review")
    url: Optional[str] = Field(None, description="The URL of the smartphone review")
    content: Optional[str] = Field(None, description="The main content of the smartphone review")
    pros: Optional[List[str]] = Field(None, description="The pros of the smartphone")
    cons: Optional[List[str]] = Field(None, description="The cons of the smartphone")
    highlights: Optional[dict] = Field(None, description="The highlights of the smartphone")
    score: Optional[float] = Field(None, description="The score of the smartphone")

class State(TypedDict):
    query: str
    products: list[dict]
    product_schema: list[SmartphoneReview]
    blogs_content: Optional[List[dict]]
    best_product: dict
    comparison: list
    youtube_link: str