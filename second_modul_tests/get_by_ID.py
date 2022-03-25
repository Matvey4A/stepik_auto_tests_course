from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def person_login():

    site_link = "http://suninjuly.github.io/find_xpath_form"
    browser = webdriver.Chrome()
    browser.get(site_link)

    try:
        input1 = browser.find_element(By.NAME, "first_name")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.NAME, "last_name")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.NAME, "firstname")
        input3.send_keys("Smolensk")
        input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")
        button = browser.find_element(
            By.XPATH, "/html/body/div/form/div[6]/button[3]")
        button.click()
    finally:
        time.sleep(30)
        browser.quit()


def find_right_link():

    site_link = "http://suninjuly.github.io/find_link_text"

    try:
        browser = webdriver.Chrome()
        browser.get(site_link)

        link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
        link = browser.find_element(By.LINK_TEXT, link_text)
        link.click()

        input1 = browser.find_element(By.NAME, "first_name")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.NAME, "last_name")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.NAME, "firstname")
        input3.send_keys("Smolensk")
        input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")
        button = browser.find_element(By.CSS_SELECTOR, ".btn")
        button.click()
    finally:
        time.sleep(15)
        browser.quit()


if __name__ == "__main__":
    print("start")
    try:
        person_login()
        print("complete")
    except:
        print("error")
