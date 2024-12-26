from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import json

driver = webdriver.Firefox()
driver.get("https://www.easylaw.ai")
driver.implicitly_wait(5) 


search_input = driver.find_element(By.ID, 'comment2')
search_input.clear()
search_input.send_keys("PLD")


search_button = driver.find_element(By.CSS_SELECTOR, 'input[value="SEARCH"]')
search_button.click()
sleep(3) 


wait = WebDriverWait(driver, 10)
sleep(5)
link_button = driver.find_element(By.CSS_SELECTOR, "button.btn-link[name='details']")
link_button.click()

sleep(20)
td_elements = driver.find_elements(By.XPATH, "//td[@colspan]")

td_content = []

#
for td in td_elements:
    td_text = td.text.strip() 

    if td_text:
        td_content.append(td_text)

with open("extracted_td_content.json", "w") as json_file:
    json.dump(td_content, json_file, ensure_ascii=False, indent=4)

print(td_content)
driver.quit()
