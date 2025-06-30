from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

tavily_api_key = os.getenv("TAVILY_API_KEY")

tavily_client = TavilyClient(api_key=tavily_api_key)