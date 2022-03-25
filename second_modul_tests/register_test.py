from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def main():
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    try:

        elements = browser.find_elements(By.CSS_SELECTOR, "input[required]")
        for element in elements:
            element.send_keys("aboba")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text

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
