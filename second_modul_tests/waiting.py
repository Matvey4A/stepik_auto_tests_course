from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)


def calculate(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

def scrolling(element):
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)

def main():
    try:

        button = browser.find_element(By.XPATH, "//button[@id = 'book']")

        WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.XPATH, "//h5[@id = 'price']"), '$100')
        )
        button.click()

        x = browser.find_element(By.XPATH, "//span[@id = 'input_value']")
        answer = calculate(int(x.text))
        input = browser.find_element(By.XPATH, "//input[@id = 'answer']")
        scrolling(input)
        input.send_keys(answer)

        button = browser.find_element(By.XPATH, "//button[@type = 'submit']")
        scrolling(button)
        button.click()
    finally:
        time.sleep(5)
        browser.quit()


if __name__ == "__main__":
    print("start")
    try:
        main()
    except:
        print("error")
    finally:
        print("complete")
