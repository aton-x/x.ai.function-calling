import json
import time
from typing import TypeVar, Any, TypedDict
from XAIAgent import XAIAgent

from SalemWitchTrialsSource import SalemWitchTrialsSource
from JCMaxwellBiographySource import JCMaxwellBiographySource
from ElectromagnetismSource import ElectromagnetismSource

# FinalMessageContent = TypedDict('FinalMessageContent', {'message content': str, 
#                                                         'create chat elapsed time': float,
#                                                         'create final response elapsed time': float})

TSourceAgent = TypeVar('TSourceAgent')

class SourceAgent(XAIAgent):
    def __init__(self: TSourceAgent, XAI_API_KEY: str, message: str) -> None:
        super().__init__(XAI_API_KEY)
        self.model='grok-2-1212'
        self.tool_choice = 'auto'
        self.messages = [{'role': 'user', 'content': message}]
        self.tools_map = { 'get_authoritative_source': self.__get_authoritative_source }
        self.tools_definition = [{
            'type': 'function',
            'function': {
                'name': 'get_authoritative_source',
                'description': 'Get the authoritative source for a given topic',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'topic': {
                            'type': 'string',
                            'description': 'The topic, e.g. J.C. Maxwell biography'
                        }
                    },
                    'required': ['topic']
                }
            }
        }]

    def __get_authoritative_source(self: TSourceAgent, topic: str) -> dict[str, str, float]:
        result = ''
        # t = time.process_time()
        
        topic_lower = topic.lower()
        if topic_lower == 'Salem Witch Trials'.lower():
            result = SalemWitchTrialsSource('https://www.history.com/news/salem-witch-trials-hysteria-factors').Retrieve()        
        elif (topic_lower == 'James Clerk Maxwell Biography'.lower() 
              or topic_lower == 'JC Maxwell Biography'.lower() 
              or topic_lower == 'J.C. Maxwell Biography'.lower()):
            result = JCMaxwellBiographySource('https://ethw.org/James_Clerk_Maxwell').Retrieve()
        elif topic_lower == 'Electromagnetism'.lower():
            result = ElectromagnetismSource('https://www.britannica.com/science/electromagnetism/Effects-of-varying-electric-fields').Retrieve()
            
        # elapsed_time = time.process_time() - t

        return {'topic':topic, 'authoritative source': result}

    def __create_chat(self: TSourceAgent) -> Any:
        response = self.client.chat.completions.create(
                                                    model=self.model,
                                                    messages=self.messages,
                                                    tools=self.tools_definition,
                                                    tool_choice=self.tool_choice)
        # print(response.choices[0].message) 
        return response

    # def get_final_response(self: TSourceAgent) -> dict[str, float, float, float]:
    def get_final_response(self: TSourceAgent) -> dict[str, dict[str, str]]:
        final_message_content = {}
        # t = time.process_time()
        response = self.__create_chat()
        # elapsed_time_create_chat = time.process_time() - t
        
        if response.choices[0].message.tool_calls:
            for tool_call in response.choices[0].message.tool_calls:
                # Get the tool function name and arguments Grok wants to call
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)

                # Call one of the tool function defined earlier with arguments
                t = time.process_time()
                result = self.tools_map[function_name](**function_args)
                elapsed_time = time.process_time() - t
                
                final_message_content[function_name + ' ' + 'function elapsed time'] = elapsed_time
                final_message_content[function_name + ' ' + 'message content'] = result

                # Append the result from tool function call to the chat message history,
                # with "role": "tool"
                # Not needed
                self.messages.append(
                    {
                        'role': 'tool',
                        'content': json.dumps(result),
                        'tool_call_id': tool_call.id  # tool_call.id supplied in Grok's response
                    }
                )
          
        # this is not needed as in this case, the completion will provide a summary   
        # t = time.process_time()   
        # final_response = self.client.chat.completions.create(
        #     model=self.model,
        #     messages=self.messages,
        #     tools=self.tools_definition,
        #     tool_choice=self.tool_choice
        # )
        # elapsed_time_create_final_response = time.process_time() - t

        # print(final_response.choices[0].message.content)
        
        # final_message_content['message content'] = final_response.choices[0].message.content
        # # final_message_content['create chat elapsed time'] = elapsed_time_create_chat
        # final_message_content['create final response elapsed time'] = elapsed_time_create_final_response
        
        # for message in self.messages:
        #     if 'function elapsed time' in message['content']:
        #         final_message_content['function elapsed time'] = json.loads(message['content'])['function elapsed time']
        #         break
            
            
        return final_message_content

