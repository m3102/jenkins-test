import os
import xmlrunner
from unittest import TestCase, main
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class UITest(TestCase):
    # Constants
    EXEC_PATH = "./drivers/chrome/v90/chromedriver"
    BASE_URL = "https://rchan.sitict.net"

    def intializeDriver(self, url):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        os.chmod(self.EXEC_PATH, 0o755)
        driver = webdriver.Chrome(self.EXEC_PATH, options=options)
        driver.get(f"{self.BASE_URL}{url}")
        return driver

    def test_login_page(self):
        driver = self.intializeDriver("/form/login")
        # Find elements on page
        emailInput = driver.find_element(By.NAME, "email")
        passwordInput = driver.find_element(By.NAME, "password")
        # Ensure input elements are of correct type
        self.assertEqual("email", emailInput.get_attribute("type"))
        self.assertEqual("password", passwordInput.get_attribute("type"))

    def test_signup_page(self):
        driver = self.intializeDriver("/form/signup")
        # Find elements on page
        usernameInput = driver.find_element(By.NAME, "username")
        emailInput = driver.find_element(By.NAME, "email")
        passwordInput = driver.find_element(By.NAME, "password")
        confirmPasswordInput = driver.find_element(By.NAME, "confirmPassword")
        checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
        # Ensure input elements are of correct type
        self.assertEqual("text", usernameInput.get_attribute("type"))
        self.assertEqual("email", emailInput.get_attribute("type"))
        self.assertEqual("password", passwordInput.get_attribute("type"))
        self.assertEqual("password", confirmPasswordInput.get_attribute("type"))
        self.assertEqual(False, checkbox.is_selected())

    def test_forgotpassword_page(self):
        driver = self.intializeDriver("/form/forgotpassword")
        # Find elements on page
        emailInput = driver.find_element(By.NAME, "email")
        # Ensure input elements are of correct type
        self.assertEqual("email", emailInput.get_attribute("type"))


if __name__ == "__main__":
    runner = xmlrunner.XMLTestRunner(output="../ui-test-report")
    main(testRunner=runner)
    # main()
