from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

print ('Hello World 1')

# Create a new instance of the Chrome driver
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# Navigate to the URL
driver.get('https://www.kexp.org/playlist/')

print ('Hello World 2')
