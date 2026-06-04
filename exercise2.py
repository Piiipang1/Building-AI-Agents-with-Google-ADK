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

# Define the agent
welcome_agent = LlmAgent(
    name="WelcomeAgent",
    description="An agent that welcomes the user.", 
    instruction="Always greet the user politely.",  
    model=AGENT_MODEL
)

# Set up session service and create a session
session_service = InMemorySessionService()
await session_service.create_session(
    app_name=APP_NAME, 
    user_id=USER_ID, 
    session_id=SESSION_ID
)

# Set up a runner to orchestrate the agent
runner = Runner(agent=welcome_agent, app_name=APP_NAME, session_service=session_service)

# Define an asynchronous function to send a query to the agent and handle its response
async def call_agent_async(query: str):
    print(f"\n>>> User Query: {query}")

    # Package the user's query into ADK format
    content = types.Content(role='user', parts=[types.Part(text=query)])
    final_response_text = "Agent did not produce a final response."

    # Iterate through streamed agent responses
    async for event in runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=content):
        if event.is_final_response(): # Check if this is the final message from the agent
            if event.content and event.content.parts:
                final_response_text = event.content.parts[0].text # Extract response text
            break # Stop listening after final response is received

    print(f"<<< Agent Response: {final_response_text}")

# Run the interaction
await call_agent_async("I have question!")