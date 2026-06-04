from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

AGENT_MODEL = LiteLlm(model="openai/gpt-4o-mini")

agent = LlmAgent(
    name="WelcomeAgent",
    description="An agent that welcomes the user.",
    instruction="Always greet the visitors politely",
    model=AGENT_MODEL
)

print(f"Agent '{agent.name}' created.")