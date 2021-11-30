from typing import KeysView
from selenium import webdriver
import random
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# # LOCAL SERVER WITH GECKODRIVER
options = Options()
options.headless = True

driver = webdriver.Firefox(executable_path='./geckodriver', options=options)
wait = WebDriverWait(driver, 10000) # Huge amount of delay response
