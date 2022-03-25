from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calculate(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def main():
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    try:
        img = browser.find_element(By.XPATH, "//img")
        value_x = img.get_attribute("valuex")
        input1 = browser.find_element(By.XPATH, "//input[@id = 'answer']")
        input1.send_keys(calculate(int(value_x)))
        checkbox = browser.find_element(
            By.XPATH, "//input[@type = 'checkbox']")
        checkbox.click()
        radio_button = browser.find_element(
            By.XPATH, "//input[@id = 'robotsRule']")
        radio_button.click()
        submit_button = browser.find_element(
            By.XPATH, "//button[@type = 'submit']")
        submit_button.click()
    finally:
        time.sleep(10)
        browser.quit()


if __name__ == "__main__":
    print("start")
    try:
        main()
        print("complete")
    except:
        print("error")
