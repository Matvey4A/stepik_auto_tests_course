from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def cycle_input():
    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/huge_form.html")
        elements = browser.find_elements(By.CSS_SELECTOR, "input")
        for element in elements:
            element.send_keys("Мой ответ")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

    finally:
        time.sleep(10)
        browser.quit()


if __name__ == "__main__":
    print("start")
    try:
        cycle_input()
        print("complete")
    except:
        print("error")
