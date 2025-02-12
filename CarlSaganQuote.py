from typing import TypeVar
from AuthorQuote import AuthorQuote

TCarlSaganQuote = TypeVar('TCarlSaganQuote')

class CarlSaganQuote(AuthorQuote):
    def __init__(self: TCarlSaganQuote, url: str) -> None:
        super().__init__(url)
    
    def Retrieve(self: TCarlSaganQuote) -> str:
        super().Retrieve()
        if self.parsed_html != '':
            try:
                quoteText = self.parsed_html.body.find_all('div', attrs={'class': 'quoteText'})
                quotes = [div.text.strip(' .\n“”') for div in quoteText]
                quotes = [quote[:quote.find('”')] for quote in quotes]
                self.long_quote = '. '.join(quotes)
            except Exception as e:
                pass
        return self.long_quote