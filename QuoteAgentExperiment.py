import json
import os
import itertools
from SourceAgent import SourceAgent
from QuoteAgent import QuoteAgent

XAI_API_KEY = os.getenv("XAI_API_KEY")

if __name__ == "__main__":
    
    if not os.path.exists("quotes"): 
        os.makedirs("quotes")
        
    iterations = 40
        
    SalemWitchTrials_source = (SourceAgent(XAI_API_KEY, 'Get the authoritative source for Salem Witch Trials.')
                               .get_final_response())
    
    JCMaxwellBiography_source = (SourceAgent(XAI_API_KEY, 'What is the authoritative source for J C Maxwell Biography?')
                                 .get_final_response())
    
    Electromagnetism_source = (SourceAgent(XAI_API_KEY, 'I wonder what the authoritative source for Electromagnetism is.')
                               .get_final_response())
    
    SalemWitchTrials_message = (f"""Analyze this writing example and mimic its style, tone, and voice in your responses: 
                                {SalemWitchTrials_source['get_authoritative_source message content']['authoritative source']}.
                                Maintain this same writing style in all your responses.""")
    
    JCMaxwellBiography_message = (f"""Analyze this writing example and mimic its style, tone, and voice in your responses: 
                                  {JCMaxwellBiography_source['get_authoritative_source message content']['authoritative source']}.
                                  Maintain this same writing style in all your responses.""")
    
    Electromagnetism_message = (f"""Analyze this writing example and mimic its style, tone, and voice in your responses: 
                                {Electromagnetism_source['get_authoritative_source message content']['authoritative source']}.
                                Maintain this same writing style in all your responses.""")
    
    WildfireCalifornia_prompt = f"""Write a post about this news: Wildfire in California"""
    GlobalPoverty2024_prompt = f"""Write a post about this news: Poverty Around the World in 2024"""
    ClimateChange_prompt = f"""Write a post about this news: Climate Change"""
    
    messages = [SalemWitchTrials_message, JCMaxwellBiography_message, Electromagnetism_message]
    prompts = [WildfireCalifornia_prompt, GlobalPoverty2024_prompt, ClimateChange_prompt]
    
    response_results = {}
    
    for iteration in range(iterations):
        print('Iteration %d.' % iteration)
        for product_tuple in itertools.product(messages, prompts):
            response = QuoteAgent(XAI_API_KEY, product_tuple[0], product_tuple[1]).generate_response()
            response['iteration'] = iteration
            if product_tuple in response_results:
                response_results[product_tuple].append(response)            
            else:
                response_results[product_tuple] = [response] 
    
    message_names = ['salem_witch_trials', 'j_c_maxwell_biography', 'electromagnetism']
    prompt_names = ['wildfire_california', 'global_poverty_2024', 'climate_change']
    
    message_mapping = {}
    prompt_mapping = {}
    
    for message, message_name in zip(messages, message_names):
        message_mapping[message] = message_name
        
    for prompt, prompt_name in zip(prompts, prompt_names):
        prompt_mapping[prompt] = prompt_name
        
    for product_tuple in itertools.product(messages, prompts):
        with open('quotes/' + message_mapping[product_tuple[0]] + '_' + prompt_mapping[product_tuple[1]] + '.json', 'w', encoding='utf-8') as write_file:
            final_result = {}
            final_result['message'] = product_tuple[0]
            final_result['prompt'] = product_tuple[1]
            final_result['results'] = response_results[product_tuple]
            json.dump(final_result, write_file, indent=4, ensure_ascii=False)    
      