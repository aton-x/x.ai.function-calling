import os
import json
from openai import OpenAI

XAI_API_KEY = os.getenv("XAI_API_KEY")

client = OpenAI(
    api_key=XAI_API_KEY,
    base_url="https://api.x.ai/v1",
)

def get_current_temperature(location: str, unit: str = "fahrenheit"):
    temperature: int
    if unit.lower() == "fahrenheit":
        temperature = 59
    elif unit.lower() == "celsius":
        temperature = 15
    else:
        raise ValueError("unit must be one of fahrenheit or celsius")
    return {"location": location, "temperature": temperature, "unit": "fahrenheit"}


def get_current_ceiling(location: str):
    return {
        "location": location,
        "ceiling": 15000,
        "ceiling_type": "broken",
        "unit": "ft",
    }

tools_map = {
    "get_current_temperature": get_current_temperature,
    "get_current_ceiling": get_current_ceiling,
}

tools_definition = [
    {
        "type": "function",
        "function": {
            "name": "get_current_temperature",
            "description": "Get the current temperature in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "default": "celsius"
                    }
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_ceiling",
            "description": "Get the current cloud ceiling in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA"
                    }
                },
                "required": ["location"]
            }
        }
    }
]

messages = [{"role": "user", "content": "What's the cloud ceiling in Livingston, NJ?"}]
response = client.chat.completions.create(
    model="grok-2-1212",
    messages=messages,
    tools=tools_definition,
    tool_choice="auto",
)

print(response.choices[0].message) 

if response.choices[0].message.tool_calls:
    for tool_call in response.choices[0].message.tool_calls:
        # Get the tool function name and arguments Grok wants to call
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments)

        # Call one of the tool function defined earlier with arguments
        result = tools_map[function_name](**function_args)

        # Append the result from tool function call to the chat message history,
        # with "role": "tool"
        messages.append(
            {
                "role": "tool",
                "content": json.dumps(result),
                "tool_call_id": tool_call.id  # tool_call.id supplied in Grok's response
            }
        )
        
final_response = client.chat.completions.create(
    model="grok-2-1212",
    messages=messages,
    tools=tools_definition,
    tool_choice="auto"
)

print(final_response.choices[0].message.content)
