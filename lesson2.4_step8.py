from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(1212)
    browser.get(link)

    button = browser.find_element(By.ID, "book")
    price_txt = browser.find_element(By.XPATH, "//h5[text()='$100']")

    button.click()

    browser.execute_script("window.scrollBy(0, 100);")

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    y_element = browser.find_element(By.ID, "answer")
    y_element.send_keys(str(y))

    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
