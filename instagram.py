#Created by Matt Cornwell

from login import *
from likes import *

driver = webdriver.Chrome(executable_path = '/usr/local/bin/chromedriver')

login(driver)
likePhoto(driver)
