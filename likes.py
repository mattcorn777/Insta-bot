#Created by Matt Cornwell

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def likePhoto(driver):
    driver.get('https://www.tutorialspoint.com/python/python_functions.htm');

    driver.quit()

    return driver;
