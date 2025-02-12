from typing import TypeVar
from AuthorQuote import AuthorQuote

TEdgarAllanPoeQuote = TypeVar('TEdgarAllanPoeQuote')

class EdgarAllanPoeQuote(AuthorQuote):
    def __init__(self: TEdgarAllanPoeQuote, url: str) -> None:
        super().__init__(url)
    
    def Retrieve(self: TEdgarAllanPoeQuote) -> str:
        super().Retrieve()
        if self.parsed_html != '':
            try:
                quoteText = self.parsed_html.body.find_all('ol')
                quotes = [li.text for li in quoteText[0]]
                quotes = [quote.strip(' .\n“”') for quote in quotes]
                self.long_quote = '. '.join(quotes)
            except Exception as e:
                pass
        return self.long_quote

