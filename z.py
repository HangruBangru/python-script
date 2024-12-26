import json
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
sleep(5)

wait = WebDriverWait(driver, 10)
sleep(5)

link_button = driver.find_element(By.CSS_SELECTOR, "button.btn-link[name='details']")
link_button.click()
sleep(10)


br_elements = driver.find_elements(By.TAG_NAME, "br")
text_content = []

for br in br_elements:
    try:
        previous_element = br.find_element(By.XPATH, "preceding-sibling::*[1]")
        previous_text = previous_element.text if previous_element else ""
    except:
        previous_text = ""
    try:
        following_element = br.find_element(By.XPATH, "following-sibling::*[1]")
        following_text = following_element.text if following_element else ""
    except:
        following_text = ""
    combined_text = previous_text + " " + following_text
    
    if combined_text.strip():
        text_content.append(combined_text.strip())
with open("extracted_br_content.json", "w") as json_file:
    json.dump(text_content, json_file, ensure_ascii=False, indent=4)

driver.quit()
