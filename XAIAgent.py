from typing import TypeVar
from openai import OpenAI

TXAIAgent = TypeVar('TXAIAgent')

class XAIAgent():
    
    def __init__(self: TXAIAgent, XAI_API_KEY: str) -> None:
        self.client = OpenAI(
            api_key=XAI_API_KEY,
            base_url='https://api.x.ai/v1',
        )