from typing import Optional

from openai import OpenAI
from pydantic import BaseModel


class OpenAIGPT:
    def __init__(self, model_name: str, api_key: str, system_prompt: Optional[str] = None):
        self.model_name = model_name
        self.api_key = api_key
        self.system_prompt = system_prompt
        self.client = OpenAI(api_key=api_key)
        self.system_prompt = system_prompt if system_prompt else "You are a helpful assistant."

    def completions(self, prompt: str, response_format: Optional[BaseModel] = None) -> str | BaseModel:
        if response_format:
            return self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt},
                ],
                response_format=response_format,
            )

        return self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt},
            ],
        )
