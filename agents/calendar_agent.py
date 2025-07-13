from pydantic import BaseModel

from agents.basic_agent import BaseAgent
from agents.models.langchain_adapter import LangchainAdapter


class CalendarAgentResponse(BaseModel):
    title: str | None = None
    description: str | None = None
    start_datetime: str | None = None
    end_datetime: str | None = None
    location: str | None = None
    timezone: str | None = None


class CalendarAgent(BaseAgent):
    def __init__(self):
        self.model_adapter = LangchainAdapter()
        self.prompt_name = "calendar-data-extractor"

    def run(self) -> CalendarAgentResponse | str | dict:
        return self.model_adapter.invoke(self.prompt_name, response_model=CalendarAgentResponse)
