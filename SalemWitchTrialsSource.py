from typing import TypeVar
from AuthoritativeSource import AuthoritativeSource
from bs4 import BeautifulSoup

TSalemWitchTrialsSource = TypeVar('TSalemWitchTrialsSource')

class SalemWitchTrialsSource(AuthoritativeSource):
    def __init__(self: TSalemWitchTrialsSource, url: str) -> None:
        super().__init__(url)
    
    def Retrieve(self: TSalemWitchTrialsSource) -> str:
        super().Retrieve()
        if self.parsed_html != '':
            try:
                quoteText = self.parsed_html.body.find_all('p')
                quotes = [p.text.strip(' .\n“”') for p in quoteText if 'class' in p.attrs and 'one' in p.attrs['class']]
                quotes = [p.text.strip(' .\n“”').replace('\xa0', '') for p in quoteText if 'article-content' in p.parent.attrs['class']]
                
                self.long_quote = '. '.join(quotes)
            except Exception as e:
                pass
        return self.long_quote   