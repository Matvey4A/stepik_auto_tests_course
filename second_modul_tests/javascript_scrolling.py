from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calculate(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

def main():
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    try:
        x = int(browser.find_element(By.XPATH, "//span[@id = 'input_value']").text)
        browser.find_element(By.XPATH, "//input[@type = 'text']").send_keys(calculate(x))

        checkbox = browser.find_element(By.XPATH, "//input[@type = 'checkbox']")
        browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
        checkbox.click()
        radio_button = browser.find_element(By.XPATH, "//input[@id = 'robotsRule']")
        browser.execute_script("return arguments[0].scrollIntoView(true);", radio_button)
        radio_button.click()

        button = browser.find_element(By.TAG_NAME, "button")
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()
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
