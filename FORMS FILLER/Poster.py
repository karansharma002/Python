from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import os
driver = webdriver.Chrome('chromedriver')

driver.get('https://www.epicgames.com/id/login')
input()
