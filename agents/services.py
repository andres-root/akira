from agents.calendar_agent import CalendarAgent, CalendarAgentResponse


class CalendarService:
    def __init__(self):
        self.calendar_agent = CalendarAgent()

    def parse_event(self, prompt: str) -> CalendarAgentResponse:
        event = self.calendar_agent.run(prompt)
        if not event:
            raise ValueError("Invalid event response")
        print("DEBUG: ", event)
        return event
