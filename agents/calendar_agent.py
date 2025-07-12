from django.conf import settings
from pydantic import BaseModel

from agents.basic_agent import BaseAgent
from agents.models.openai_gpt import OpenAIGPT


class CalendarAgentResponse(BaseModel):
    name: str
    description: str
    date: str
    participants: list[str]
    location: str


class CalendarAgent(BaseAgent):
    def __init__(self):
        self.model = OpenAIGPT(
            api_key=settings.OPENAI_API_KEY,
            model_name="gpt-4o-mini",
            system_prompt="You are a helpful assistant that can help me create a calendar event.",
        )

    def run(self, prompt: str) -> CalendarAgentResponse | str:
        return self.model.completions(prompt, CalendarAgentResponse)
