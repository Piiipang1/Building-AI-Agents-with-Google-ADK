from google.adk.tools import FunctionTool
from google.genai import types
from google import genai
from google.adk.models.lite_llm import LiteLlm
import litellm 

AGENT_MODEL = LiteLlm(model="openai/gpt-4o-mini")
APP_NAME = "adk_course_app"
USER_ID = "user_123"
SESSION_ID = "support_session"

# Define the FAQ knowledge base
FAQ_DATA = {
    "return policy": "You can return items within 30 days of purchase.",
    "hours": "Our support team is available from 9am to 5pm, Monday to Friday.",
    "contact": "You can reach support at help@example.com."
}

def lookup_faq(question: str) -> str:
    faq_text = "\n".join(f"- {k}: {v}" for k, v in FAQ_DATA.items())
    prompt = (
        f"You are a helpful assistant. Here is a list of FAQs:\n\n{faq_text}\n\n"
        f"User question: \"{question}\". "
        f"Reply with the best match or say you don't know."
    )
    response = litellm.completion(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"].strip()

# Wrap the tool
faq_tool = FunctionTool(func=lookup_faq)

support_agent = LlmAgent(
    name="SupportAgent",
    description="An agent that answers users' questions based on a set of FAQs.",
    instruction="Use the FAQ tool to help answer customer questions.",
    model=AGENT_MODEL,
    tools=[faq_tool]
)