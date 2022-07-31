from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    y_element = browser.find_element(By.ID, "answer")
    y_element.send_keys(str(y))

    cbox = browser.find_element(By.ID, "robotCheckbox")
    cbox.click()

    rbox = browser.find_element(By.ID, "robotsRule")
    rbox.click()

    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
