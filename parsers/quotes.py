from selenium.webdriver.common.by import By
from locators.quote_locators import QuoteLocators


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
        locator = QuoteLocators.QUOTE
        return self.parent.find_element(By.CSS_SELECTOR, locator).text

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.find_element(By.CSS_SELECTOR, locator).text

    @property
    def tags(self):
        locator = QuoteLocators.TAG
        return [tag.string for tag in self.parent.find_elements(By.CSS_SELECTOR, locator)]