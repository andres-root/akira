from django.conf import settings
from pydantic import BaseModel

from agents.basic_agent import BaseAgent
from agents.models import AnthropicClaude, OpenAIGPT


class CalendarAgentResponse(BaseModel):
    title: str | None = None
    description: str | None = None
    start_datetime: str | None = None
    end_datetime: str | None = None
    location: str | None = None
    timezone: str | None = None


class CalendarAgent(BaseAgent):
    def __init__(self):
        self.claude = AnthropicClaude(
            api_key=settings.ANTHROPIC_API_KEY,
            model="claude-3-5-haiku-20241022",
            system_prompt="You are a helpful assistant that can extract the name, a short description of max 248 characters, date, participants, and location from a calendar event in a given text.",
        )
        self.gpt = OpenAIGPT(
            api_key=settings.OPENAI_API_KEY,
            model_name="gpt-4o-mini",
            system_prompt="You are a helpful assistant that can extract the name, a short description of max 248 characters, date, participants, and location from a calendar event in a given text.",
        )
        self.model = self.claude

    def run(self, prompt: str) -> CalendarAgentResponse | str:
        return self.model.run(prompt, CalendarAgentResponse)
