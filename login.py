#Created by Matt Cornwell

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def login(driver):

    user = '' #Enter your username here
    pwd = '' #Enter your password here
    
    driver.get('https://www.instagram.com/accounts/login/');

    username = driver.find_element_by_name('username')
    password = driver.find_element_by_name('password')

    username.send_keys(user)
    password.send_keys(pwd)

    password.send_keys(Keys.RETURN)

    return driver;
