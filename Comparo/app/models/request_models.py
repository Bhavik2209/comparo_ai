from pydantic import BaseModel
from typing import Optional

class ComparisonRequest(BaseModel):
    query: str
    max_results: Optional[int] = 1