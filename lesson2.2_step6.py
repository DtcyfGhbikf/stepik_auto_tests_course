from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

    y_element = browser.find_element(By.ID, "answer")
    y_element.send_keys(str(y))

    cbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    cbox.click()

    rbox = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    rbox.click()

    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
