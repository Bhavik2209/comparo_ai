from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

youtube_api_key = os.getenv("YOUTUBE_API_KEY")

#Youtube api for video search
youtube = build('youtube', 'v3', developerKey=youtube_api_key)