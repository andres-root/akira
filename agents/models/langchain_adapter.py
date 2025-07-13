import logging

from django.conf import settings
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langsmith import Client
from pydantic import BaseModel

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class LangchainAdapter:
    def __init__(self):
        self.langsmith_client = Client(api_key=settings.LANGSMITH_API_KEY)
        self.anthropic = ChatAnthropic(
            api_key=settings.ANTHROPIC_API_KEY,
            model="claude-3-5-haiku-20241022",
            temperature=1,
            max_tokens=1000,
        )
        self.openai = ChatOpenAI(
            api_key=settings.OPENAI_API_KEY,
            model="gpt-4o-mini",
            temperature=1,
        )
        self.model = self.anthropic

    def invoke(self, prompt_name: str, response_model: BaseModel) -> dict | BaseModel:
        try:
            prompt = self.langsmith_client.pull_prompt(prompt_name)
            chain = prompt | self.model | StrOutputParser(pydantic_object=response_model)
            result = chain.invoke()
            return result
        except Exception as e:
            logger.error(f"Error invoking model: {e}")
            return None
