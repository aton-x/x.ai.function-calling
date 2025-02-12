from typing import TypeVar
from AuthorQuote import AuthorQuote

TAlbertEinsteinQuote = TypeVar('TAlbertEinsteinQuote')

class AlbertEinsteinQuote(AuthorQuote):
    def __init__(self: TAlbertEinsteinQuote, url: str) -> None:
        super().__init__(url)
    
    def Retrieve(self: TAlbertEinsteinQuote) -> str:
        super().Retrieve()
        if self.parsed_html != '':
            try:
                quoteText = self.parsed_html.body.find_all('p')
                quotes = [p.strong.text for p in quoteText if p.strong is not None]
                quotes = [quote[quote.find('.')+1:] for quote in quotes]
                quotes = [quote.strip(' .\n“”') for quote in quotes]
                self.long_quote = '. '.join(quotes)
            except Exception as e:
                pass
        return self.long_quote