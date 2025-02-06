import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.quotes_page import QuotePage, InvalidTagForAuthorError

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S', level=logging.INFO, filename='log.txt')

logger = logging.getLogger('scraping')

logger.info('Loading Quotes from celebrities...')

try:
    author = input('Enter your favourite author: ')
    selected_tags = input("Enter your tags: ")

    chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    chrome.get("https://quotes.toscrape.com/search.aspx")

    page = QuotePage(chrome)

    print(page.search_for_quote(author, selected_tags))

except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print("An Unknown error... Try again")