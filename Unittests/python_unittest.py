import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, "//input[@placeholder = 'Input your first name']")
        input1.send_keys("Name")
        input2 = browser.find_element(By.XPATH, "//input[@placeholder = 'Input your last name']")
        input2.send_keys("Last name")
        input3 = browser.find_element(By.XPATH, "//input[@placeholder = 'Input your email']")
        input3.send_keys("Email")
        input4 = browser.find_element(By.XPATH, "//input[@placeholder = 'Input your phone:']")
        input4.send_keys("phone")
        input5 = browser.find_element(By.XPATH, "//input[@placeholder = 'Input your address:']")
        input5.send_keys("address")

        button = browser.find_element(By.XPATH, "//button[@type = 'submit']")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(
            "Congratulations! You have successfully registered!", welcome_text,
            "Text isn't right"
            )
        browser.quit()

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, "//input[@placeholder = 'Input your first name']")
        input1.send_keys("Name")
        input2 = browser.find_element(By.XPATH, "//input[@placeholder = 'Input your last name']")
        input2.send_keys("Last name")
        input3 = browser.find_element(By.XPATH, "//input[@placeholder = 'Input your email']")
        input3.send_keys("Email")
        input4 = browser.find_element(By.XPATH, "//input[@placeholder = 'Input your phone:']")
        input4.send_keys("phone")
        input5 = browser.find_element(By.XPATH, "//input[@placeholder = 'Input your address:']")
        input5.send_keys("address")

        button = browser.find_element(By.XPATH, "//button[@type = 'submit']")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(
            "Congratulations! You have successfully registered!", welcome_text,
            "Text isn't right"
            )
        browser.quit()


if __name__ == "__main__":
    unittest.main()
