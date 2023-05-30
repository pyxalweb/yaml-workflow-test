from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

print ('Hello World 1')

# Create a new instance of the Firefox driver
driver = webdriver.Chrome()

# Navigate to the URL
driver.get('https://www.kexp.org/playlist/')

print ('Hello World 2')
