from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import json

driver = webdriver.Firefox()

driver.get("https://www.easylaw.ai")

search_input = driver.find_element(By.ID, 'comment2')
search_input.clear()
search_input.send_keys("PLD")


search_button = driver.find_element(By.CSS_SELECTOR, 'input[value="SEARCH"]')
search_button.click()
sleep(10)


wait = WebDriverWait(driver, 10)
sleep(10)

link_button = driver.find_element(By.CSS_SELECTOR, "button.btn-link[name='details']")
link_button.click()
sleep(20)

html_content = driver.page_source

html_data = {
    "html_content": html_content
}

with open("page_html_content.json", "w") as json_file:
    json.dump(html_data, json_file, ensure_ascii=False, indent=4)

print("HTML content has been saved to page_html_content.json")

driver.quit()
