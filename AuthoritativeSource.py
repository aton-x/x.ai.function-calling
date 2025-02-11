from typing import TypeVar
from urllib import request, parse
from bs4 import BeautifulSoup

TAuthoritativeSource = TypeVar('TAuthoritativeSource')

class AuthoritativeSource:
    def __init__(self: TAuthoritativeSource, url: str) -> None:
        self.url = url
        self.head = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Charset": "ISO-8859-1,utf-8,utf-16;q=0.7,*;q=0.3",
            "Accept-Encoding": "none",
            "Accept-Language": "en-US,en;q=0.8",
            "Connection": "keep-alive",
            "refere": parse.urlparse(url).netloc,
            "cookie": """dummy cookie""",
        }
        self.parsed_html = ''
        self.long_quote = ''
    
    def Retrieve(self: TAuthoritativeSource) -> str:
        try:
            req = request.Request(self.url, headers=self.head)
            response = request.urlopen(req).read().decode('UTF-8')
            self.parsed_html = BeautifulSoup(response)
        except Exception as e:
            pass