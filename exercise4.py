from google.genai import types

safety_settings = [
    types.SafetySetting(
        category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    ),
]

generate_content_config = types.GenerateContentConfig(
   safety_settings=safety_settings,
   temperature=0.28,
   max_output_tokens=1000,
   top_p=0.95,
)

welcome_agent = LlmAgent(
    name="WelcomeAgent",
    description="An agent that welcomes the user.",
    instruction="Always greet the user politely. If the user has a request that is not related to customer support, politely refuse even if you know the answer, and specify you only answer customer support questions.",
    model=AGENT_MODEL,
    generate_content_config=generate_content_config
)

print(f"Agent '{welcome_agent.name}' created.")

# Install and import required libraries
import nest_asyncio
import asyncio
nest_asyncio.apply()  # Required for async in notebooks

from google.genai.client import Client 
from google.adk.models import Gemini
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

# Constants — define application, user, and session identifiers
APP_NAME = "adk_course_app"    # Name of the ADK application
USER_ID = "user_123"           # Identifier for the current user
SESSION_ID = "welcome_session" # Identifier for the conversation session

# Set up session service and create a session
session_service = InMemorySessionService()
await session_service.create_session(
    app_name=APP_NAME, 
    user_id=USER_ID, 
    session_id=SESSION_ID
)

# Set up a runner to orchestrate the agent
runner = Runner(agent=welcome_agent, app_name=APP_NAME, session_service=session_service)