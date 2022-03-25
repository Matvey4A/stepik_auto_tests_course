from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calculate(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

def main():
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    try:
        browser.find_element(By.XPATH, "//button[@type='submit']").click()

        alert = browser.switch_to.alert
        alert_text = alert.text
        alert.accept()

        time.sleep(1)

        x = int(browser.find_element(By.XPATH, "//span[@id = 'input_value']").text)
        input = browser.find_element(By.XPATH, "//input[@id = 'answer']")
        input.send_keys(calculate(x))

        browser.find_element(By.XPATH, "//button[@type = 'submit']").click()
    finally:
        time.sleep(10)
        browser.quit()


if __name__ == "__main__":
    print("start")
    try:
        main()
    except:
        print("error")
    finally:
        print("complete")
