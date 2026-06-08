# Install and import required libraries
import nest_asyncio
import asyncio
nest_asyncio.apply()  # Required for async in notebooks

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

# Constants — define application, user, and session identifiers
APP_NAME      = "adk_course_app"
USER_ID       = "user_123"
SESSION_ID    = "support_session"

# FAQ knowledge base & tool 
FAQ_DATA = {
    "return policy": "You can return items within 30 days of purchase.",
    "hours": "Our support team is available from 9 am to 5 pm, Monday to Friday.",
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

faq_tool  = FunctionTool(func=lookup_faq)