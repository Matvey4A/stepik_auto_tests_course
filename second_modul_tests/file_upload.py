from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


def main():
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    try:
        elements = browser.find_elements(By.CLASS_NAME, "form-control")
        for element in elements:
            element.send_keys("aboba")
        file_element = browser.find_element(By.XPATH, "//*[@id='file']")
        file_element.send_keys(file_path)

        button = browser.find_element(By.XPATH, "//button[@type='submit']")
        button.click()

        alert = browser.switch_to.alert
        alert_text = alert.text
        alert.accept()
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
