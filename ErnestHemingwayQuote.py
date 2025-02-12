from typing import TypeVar
from AuthorQuote import AuthorQuote

TErnestHemingwayQuote = TypeVar('TErnestHemingwayQuote')

class ErnestHemingwayQuote(AuthorQuote):
    def __init__(self: TErnestHemingwayQuote, url: str) -> None:
        super().__init__(url)
    
    def Retrieve(self: TErnestHemingwayQuote) -> str:
        super().Retrieve()
        if self.parsed_html != '':
            try:
                quoteText = self.parsed_html.body.find_all('div', attrs={'style': 'display: flex;justify-content: space-between'})
                quotes = [div.text for div in quoteText]
                quotes = [quote.strip(' .\n“”') for quote in quotes]
                self.long_quote = '. '.join(quotes)
            except Exception as e:
                pass
        return self.long_quote
