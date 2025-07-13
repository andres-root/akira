from agents.calendar_agent import CalendarAgent, CalendarAgentResponse


class CalendarService:
    def __init__(self):
        self.calendar_agent = CalendarAgent()

    def parse_event(self) -> CalendarAgentResponse:
        event = self.calendar_agent.run()
        if not event:
            raise ValueError("Invalid event response")
        print(event)
        return event
