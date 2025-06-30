# app/core/graph_workflow.py

from langgraph.graph import StateGraph, START, END
from app.core.nodes import (
    tavily_search_node,
    schema_mapping_node, 
    product_comparison_node,
    youtube_video_node
)
from app.models.schema_models import State

def get_comparison_workflow():
    """
    Create and return the smartphone comparison workflow
    """
    # Create the workflow graph
    workflow = StateGraph(State)
    
    # Add nodes
    workflow.add_node("tavily_search", tavily_search_node)
    workflow.add_node("schema_mapping", schema_mapping_node)
    workflow.add_node("product_comparison", product_comparison_node)
    workflow.add_node("youtube_video", youtube_video_node)
    
    # Add edges to define the flow
    workflow.add_edge(START, "tavily_search")
    workflow.add_edge("tavily_search", "schema_mapping")
    workflow.add_edge("schema_mapping", "product_comparison")
    workflow.add_edge("product_comparison", "youtube_video")
    workflow.add_edge("youtube_video", END)
    
    # Compile and return the graph
    return workflow.compile()

def create_initial_state(query: str) -> dict:
    """
    Create initial state for the workflow
    """
    return {
        "query": query,
        "products": [],
        "product_schema": [],
        "blogs_content": None,
        "best_product": {},
        "comparison": [],
        "youtube_link": ""
    }