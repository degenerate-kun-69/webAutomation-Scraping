from prompt_toolkit.contrib.telnet.protocol import EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.get("https://www.w3schools.com/howto/howto_css_searchbar.asp")
search = driver.find_element(by=By.ID,value="tnb-google-search-input")
search.send_keys("selenium")
search.send_keys(Keys.RETURN)
print(driver.title)
try:
    div=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"gsc-wrapper gsc-webResult")))
    print(div.text)
except:
    driver.quit()

driver.quit()