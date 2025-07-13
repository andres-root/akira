from abc import ABC, abstractmethod

from pydantic import BaseModel


class BaseAgentResponse(BaseModel):
    message: str


class BaseAgent(ABC):
    @abstractmethod
    def run(self):
        raise NotImplementedError("Subclasses must implement this method")
