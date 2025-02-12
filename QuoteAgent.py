import json
import time
from typing import TypeVar
from XAIAgent import XAIAgent

TQuoteAgent = TypeVar('TQuoteAgent')

class QuoteAgent(XAIAgent):
    def __init__(self: TQuoteAgent, XAI_API_KEY: str, message: str, prompt: str) -> None:
        super().__init__(XAI_API_KEY)
        self.model='grok-2-1212'
        self.system_message = message
        self.messages=[
                {"role": "system", "content": message},
                {"role": "user", "content": prompt},
            ]
        
    def generate_response(self: TQuoteAgent):
        success = False
        elapsed_time = 0
        
        while not success:
            time.sleep(60)
            
            try:
                t1 = time.process_time()
                completion = self.client.chat.completions.create(
                    model=self.model,
                    messages=self.messages
                )
                t2 = time.process_time()
                elapsed_time = t2 - t1
                success = True
            except Exception as e:
                print ('Exception: %s\n' % e)

        return {'content': completion.choices[0].message.content, 'elapsed_time': elapsed_time}
        