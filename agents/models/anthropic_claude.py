from typing import Optional

from anthropic import Anthropic
from pydantic import BaseModel


class AnthropicClaude:
    def __init__(self, api_key: str, model: str, system_prompt: str):
        self.api_key = api_key
        self.model = model
        self.max_tokens = 1000
        self.client = Anthropic(api_key=self.api_key)
        self.temperature = 1
        self.system_prompt = system_prompt if system_prompt else "You are a helpful assistant."

    def run(self, prompt: str, response_format: Optional[BaseModel] = None) -> str:
        if not prompt:
            raise ValueError("Prompt is required")

        response = self.client.messages.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt},
            ],
        )
        return response.content[0].text
