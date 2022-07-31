from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    y = int(browser.find_element(By.ID, "num1").text) \
        + int(browser.find_element(By.ID, "num2").text)

    y_element = Select(browser.find_element(By.ID, "dropdown"))
    y_element.select_by_visible_text(str(y))

    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
