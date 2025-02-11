from typing import TypeVar
from AuthoritativeSource import AuthoritativeSource

TJCMaxwellBiographySource = TypeVar('TJCMaxwellBiographySource')

class JCMaxwellBiographySource(AuthoritativeSource):
    def __init__(self: TJCMaxwellBiographySource, url: str) -> None:
        super().__init__(url)
    
    def Retrieve(self: TJCMaxwellBiographySource) -> str:
        super().Retrieve()
        if self.parsed_html != '':
            try:
                quoteText = self.parsed_html.body.find_all('p')
                quotes = [p.text.strip(' .\n“”') for p in quoteText if 'class' in p.parent.attrs and 'mw-parser-output' in p.parent.attrs['class']]
                quotes = [quote for quote in quotes if len(quote) != 0]
                quotes = quotes[:-4]
                self.long_quote = '. '.join(quotes)
            except Exception as e:
                pass
        return self.long_quote   