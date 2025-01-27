from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.quotes_page import QuotePage

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.get("https://quotes.toscrape.com/search.aspx")

page = QuotePage(chrome)

author = input('Enter your favourite author: ')
page.select_author(author)

tags = page.get_available_tags()
print("Select one of these tags: [{}]".format(" | ".join(tags)))
selected_tags = input("Enter your tags: ")
page.select_tag(selected_tags)