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