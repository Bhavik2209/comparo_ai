# app/api/v1/endpoints/comparison.py

from fastapi import APIRouter, HTTPException, Depends
from app.models.request_models import ComparisonRequest
from app.models.response_models import ComparisonResponse
from app.core.graph_workflow import get_comparison_workflow

import asyncio
from typing import Dict, Any

router = APIRouter()

@router.post("/", response_model=ComparisonResponse)
async def compare_smartphones(
    request: ComparisonRequest
):
    """
    Compare smartphones based on the provided query
    
    - **query**: Search query for smartphone comparison
    - **max_results**: Maximum number of results to return (optional)
    
    Returns detailed comparison with specifications, ratings, and best product recommendation
    """
    try:
        # Get the workflow from your core module
        workflow = get_comparison_workflow()
        
        # Prepare initial state
        initial_state = {
            "query": request.query
        }
        
        # Execute the workflow
        final_state = None
        for event in workflow.stream(input=initial_state, stream_mode="updates"):
            # Process each step of the workflow
            if event:
                # Update final_state with the latest event data
                for node_name, node_data in event.items():
                    if node_data:
                        if final_state is None:
                            final_state = {}
                        final_state.update(node_data)
        
        # Check if we have valid results
        if not final_state or "comparison" not in final_state:
            raise HTTPException(
                status_code=404,
                detail="No smartphone comparison data found for the given query"
            )
        
        # Return successful response
        return ComparisonResponse(
            success=True,
            message="Smartphone comparison completed successfully",
            products=final_state.get("product_schema", []),
            best_product=final_state.get("best_product", {}),
            comparison=final_state.get("comparison", []),
            youtube_link=final_state.get("youtube_link")
        )
        
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        # Handle any other exceptions
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error during smartphone comparison: {str(e)}"
        )

@router.get("/sample")
async def get_sample_comparison():
    """
    Get a sample comparison for testing purposes
    """
    try:
        # Use default query for sample
        sample_request = ComparisonRequest(
            query="Best smartphone under 30000 India 2025 for best camera quality"
        )
        
        # Call the main comparison endpoint
     
        result = await compare_smartphones(sample_request)
        
        return result
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating sample comparison: {str(e)}"
        )