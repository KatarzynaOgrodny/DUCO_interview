import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.sign_in_button = (By.LINK_TEXT, "Sign in")

    def load(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element(By.XPATH, "//*[text()='Accept all']").click()

    def click_sign_in_button(self):
        sign_in_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.sign_in_button)
        )
        sign_in_button.click()

    def save_screenshot(self, directory, filename):
        if not os.path.exists(directory):
            os.makedirs(directory)
        filepath = os.path.join(directory, filename)
        self.driver.save_screenshot(filepath)


driver = webdriver.Chrome()
google_homepage = GoogleHomePage(driver)
google_homepage.load()
google_homepage.click_sign_in_button()
directory = "screenshots_button"
filename = "signin_button.png"
google_homepage.save_screenshot(directory, filename)
driver.quit()
