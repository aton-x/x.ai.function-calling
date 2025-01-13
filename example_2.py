import requests as req
import os
from openai import OpenAI

XAI_API_KEY = os.getenv("XAI_API_KEY")

def create_style_assistant(writing_example):
    client = OpenAI(
        api_key=XAI_API_KEY,
        base_url='https://api.x.ai/v1',
    )
    system_message = f"""Analyze this writing example and mimic its style, tone, and voice in your responses: {writing_example}. Maintain this same writing style in all your responses."""

    return client, system_message

def generate_response(client, system_message, prompt):
    completion = client.chat.completions.create(
        model="grok-beta",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt},
        ]
    )

    return completion.choices[0].message.content

if __name__ == "__main__":
    my_writing_style = """The infamous Salem witch trials began during the spring of 1692, after a group of young girls in Salem Village, Massachusetts, claimed to be possessed by the devil and accused several local women of witchcraft. As a wave of hysteria spread throughout colonial Massachusetts, a special court convened in Salem to hear the cases; the first convicted witch, Bridget Bishop, was hanged that June. Eighteen others followed Bishop to Salem’s Gallows Hill, while some 150 more men, women and children were accused over the next several months. 
                          By September 1692, the hysteria had begun to abate and public opinion turned against the trials. Though the Massachusetts General Court later annulled guilty verdicts against accused witches and granted indemnities to their families, bitterness lingered in the community, and the painful legacy of the Salem witch trials would endure for centuries."""

    # Create the assistant
    client, system_message = create_style_assistant(my_writing_style)

    # Generate a response
    prompt = f"""Write a post about this news: Wildfire in California"""
    response = generate_response(client, system_message, prompt)
    
    with open("whildfire.txt", "w") as text_file:
        text_file.write(response)
    
    print(response)    
    
    prompt = f"""Write a post about this news: Poverty Around the World in 2024"""
    response = generate_response(client, system_message, prompt)
    
    with open("powerty.txt", "w") as text_file:
        text_file.write(response)
        
    print(response)
    
    prompt = f"""Write a post about this news: Climate Change"""
    response = generate_response(client, system_message, prompt)
    
    with open("climate.txt", "w") as text_file:
        text_file.write(response)
        
    print(response)
    
    