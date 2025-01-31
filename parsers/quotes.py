import logging
from selenium.webdriver.common.by import By
from locators.quote_locators import QuoteLocators

logger = logging.getLogger('scraping.quote_parser')

class QuoteParser:
    """
    Given one of the quote div,
    find the information or data
    about the quote. The information
    in this case are (Quote text, Tags,and Author)
    """

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"Quote: {self.quote} by {self.author}"

    @property
    def quote(self):
        logger.debug('Finding a quote...')
        locator = QuoteLocators.QUOTE
        quote_text = self.parent.find_element(By.CSS_SELECTOR, locator).text
        logger.debug(f'Found quote: {quote_text}')
        return quote_text

    @property
    def author(self):
        logger.debug('Finding an author...')
        locator = QuoteLocators.AUTHOR
        found_author = self.parent.find_element(By.CSS_SELECTOR, locator).text
        logger.debug(f'Found author: {found_author}')
        return found_author

    @property
    def tags(self):
        locator = QuoteLocators.TAG
        return [tag.string for tag in self.parent.find_elements(By.CSS_SELECTOR, locator)]