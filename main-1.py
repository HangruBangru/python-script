from selenium import webdriver
import json
import urllib.parse
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep 
download_dir = "/python-learning-repo"
custom_file_name = "downloaded_case.txt" 


driver = webdriver.Firefox()

driver.get("https://www.easylaw.ai")
driver.implicitly_wait(5)

search_input = driver.find_element(By.ID, 'comment2')
search_input.clear()

search_input.send_keys("PLD")


search_input = driver.find_element(By.CSS_SELECTOR, 'input[value="SEARCH"]')
search_input.click()
driver.implicitly_wait(5)

wait = WebDriverWait(driver, 10)
link_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-link')))
link_button.click()
sleep(20)


print(driver.title)

driver.quit()
