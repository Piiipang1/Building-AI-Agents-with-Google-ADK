from google.adk.tools import FunctionTool
from google.genai import types
from google import genai
from google.adk.models.lite_llm import LiteLlm
import litellm 

AGENT_MODEL = LiteLlm(model="openai/gpt-4o-mini")
APP_NAME = "adk_course_app"
USER_ID = "user_123"
SESSION_ID = "support_session"