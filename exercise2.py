# Install and import required libraries
import nest_asyncio
import asyncio
nest_asyncio.apply()  # Required for async in notebooks

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

# Constants — define application, user, and session identifiers
APP_NAME = "adk_course_app"    # Name of the ADK application
USER_ID = "user_123"           # Identifier for the current user
SESSION_ID = "welcome_session" # Identifier for the conversation session