from selenium import webdriver
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

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

br_elements = driver.find_elements(By.TAG_NAME, "br")
text_content = []
for br in br_elements:
    previous_text = br.find_element(By.XPATH, "preceding-sibling::text()").text if br.find_element(By.XPATH, "preceding-sibling::text()") else ""
    following_text = br.find_element(By.XPATH, "following-sibling::text()").text if br.find_element(By.XPATH, "following-sibling::text()") else ""
    combined_text = previous_text + " " + following_text
    

    if combined_text.strip():
        text_content.append(combined_text.strip())

with open("extracted_br_content.json", "w") as json_file:
    json.dump(text_content, json_file, ensure_ascii=False, indent=4)


print(text_content)

print(driver.title)
driver.quit()
