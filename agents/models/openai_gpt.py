from typing import Optional

from openai import OpenAI
from pydantic import BaseModel


class OpenAIGPT:
    def __init__(self, api_key: str, model: str, system_prompt: Optional[str] = None):
        self.model = model
        self.api_key = api_key
        self.system_prompt = system_prompt
        self.client = OpenAI(api_key=self.api_key)
        self.system_prompt = system_prompt if system_prompt else "You are a helpful assistant."

    def run(self, prompt: str, response_format: Optional[BaseModel] = None) -> str | BaseModel:
        if response_format:
            return self.client.chat.completions.parse(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt},
                ],
                response_format=response_format,
            )

        return self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt},
            ],
        )
