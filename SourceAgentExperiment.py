import json
import os
from SourceAgent import SourceAgent

XAI_API_KEY = os.getenv("XAI_API_KEY")

if __name__ == "__main__":
    
    if not os.path.exists("sources"): 
        os.makedirs("sources") 

    SalemWitchTrials_source = SourceAgent(XAI_API_KEY,
                                'Get the authoritative source for Salem Witch Trials.').get_final_response()
    
    with open('sources/salem_witch_trials_source.json', 'w', encoding='utf-8') as write_file:
        json.dump(SalemWitchTrials_source, 
                  write_file,
                  indent=4,
                  ensure_ascii=False)    
    
    print('Salem Witch Trials source: {}', 
          json.dumps(SalemWitchTrials_source, 
                     indent=4,
                     ensure_ascii=False))
    
    JCMaxwellBiography_source = SourceAgent(XAI_API_KEY,
                                    'What is the authoritative source for J C Maxwell Biography?').get_final_response()
    
    with open('sources/j_c_maxwell_biography_source.json', 'w', encoding='utf-8') as write_file:
        json.dump(JCMaxwellBiography_source, 
                  write_file, 
                  indent=4,
                  ensure_ascii=False)    
    
    print('J C Maxwell Biography source: {}', 
          json.dumps(JCMaxwellBiography_source,
                     indent=4,
                     ensure_ascii=False))
    
    Electromagnetism_source = SourceAgent(XAI_API_KEY,
                                'I wonder what the authoritative source for Electromagnetism is.').get_final_response()
    
    with open('sources/electromagnetism_source.json', 'w', encoding='utf-8') as write_file:
        json.dump(Electromagnetism_source, 
                  write_file, 
                  indent=4,
                  ensure_ascii=False)    

    print('The Electromagnetism source: {}', 
          json.dumps(Electromagnetism_source,
                     indent=4,
                     ensure_ascii=False))