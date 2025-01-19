from bs4 import BeautifulSoup
from locators.quotes_page_locators import QuotePageLocators
from parsers.quotes import QuoteParser


class QuotePage:

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        locator = QuotePageLocators.QUOTES
        quote_tags = self.soup.select(locator)
        return [QuoteParser(q) for q in quote_tags]