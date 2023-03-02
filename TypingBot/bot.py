from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://10fastfingers.com/typing-test/english")
time.sleep(10)

driver.find_element(By.ID, "CybotCookiebotDialogBodyButtonDecline").click()

word_list = []
words = driver.find_elements(By.CSS_SELECTOR, "#row1>span[wordnr]")
for word in words:
    word_list.append(word.get_attribute("textContent"))


print(word_list)

for word in word_list:
    driver.find_element(By.ID, "inputfield").send_keys(word, " ")

time.sleep(500)