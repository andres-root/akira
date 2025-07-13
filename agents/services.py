from agents.calendar_agent import CalendarAgent, CalendarAgentResponse


class CalendarService:
    def __init__(self):
        self.calendar_agent = CalendarAgent()

    def parse_event(self, prompt: str) -> CalendarAgentResponse:
        response = self.calendar_agent.run(prompt)
        if not response:
            raise ValueError("Invalid event response")

        parsed_event = response.choices[0].message.parsed
        return parsed_event
