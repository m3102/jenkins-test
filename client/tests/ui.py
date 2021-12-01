import os
import xmlrunner
from unittest import TestCase, main
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class UITest(TestCase):
    # Constants
    EXEC_PATH = "./drivers/chrome/v90/chromedriver"
    BASE_URL = "http://192.168.1.93:5000"

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
        driver = self.intializeDriver("")
        # Find elements on page
        emailInput = driver.find_element(By.NAME, "username")
        # Ensure input elements are of correct type
        self.assertEqual("text", emailInput.get_attribute("type"))


if __name__ == "__main__":
    runner = xmlrunner.XMLTestRunner(output="../ui-test-report")
    main(testRunner=runner)