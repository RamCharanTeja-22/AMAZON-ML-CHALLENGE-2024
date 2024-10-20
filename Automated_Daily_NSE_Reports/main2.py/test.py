import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
url='https://www.nseindia.com/all-reports'
driver=webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)
select=driver.find_element(By.ID,"Selectall")
time.sleep(15)
driver.quit()