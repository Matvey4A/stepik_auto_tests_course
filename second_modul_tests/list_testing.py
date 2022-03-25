from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def main():
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    try:
        int1 = int(browser.find_element(By.XPATH, "//span[@id = 'num1']").text)
        int2 = int(browser.find_element(By.XPATH, "//span[@id = 'num2']").text)
        answer = int1 + int2

        select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
        select.select_by_value(str(answer))

        button = browser.find_element(By.CSS_SELECTOR, ".btn")
        button.click()
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
