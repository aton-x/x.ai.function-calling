from typing import TypeVar
from AuthoritativeSource import AuthoritativeSource

TElectromagnetismSource = TypeVar('TElectromagnetismSource')

class ElectromagnetismSource(AuthoritativeSource):
    def __init__(self: TElectromagnetismSource, url: str) -> None:
        super().__init__(url)
    
    def Retrieve(self: TElectromagnetismSource) -> str:
        super().Retrieve()
        if self.parsed_html != '':
            try:
                quoteText = self.parsed_html.body.find_all('p', attrs={'class': 'topic-paragraph'})
                quotes = [p.text.strip(' \n“”') for p in quoteText]
                self.long_quote = '. '.join(quotes)
            except Exception as e:
                pass
        return self.long_quote   