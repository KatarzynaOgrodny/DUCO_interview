from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

class GoogleHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_bar = (By.NAME, "q")
        self.search_button = (By.NAME, "btnK")

    def navigate_to(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element(By.XPATH, "//*[text()='Accept all']").click()

    def search_for(self, search_query):
        search_bar = self.driver.find_element(*self.search_bar)
        search_bar.send_keys(search_query)
        search_bar.send_keys(Keys.RETURN)

    def wait_for_search_results(self, timeout=1):
        try:
            element_present = EC.presence_of_element_located((By.ID, "search"))
            WebDriverWait(self.driver, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for search results")

    def save_screenshot(self, filename):
        self.driver.save_screenshot(filename)

class TestGoogleHomePage:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.home_page = GoogleHomePage(self.driver)

    def teardown_method(self, method):
        self.driver.quit()

    def test_search_for_selenium(self):
        self.home_page.navigate_to()
        self.home_page.search_for("selenium")
        self.home_page.wait_for_search_results()
        assert "selenium" in self.driver.title

    def take_screenshot(self, filename):
        self.home_page.save_screenshot(filename)

directory = "screenshots_searching"
if not os.path.exists(directory):
    os.makedirs(directory)

driver = webdriver.Chrome()
google_homepage = GoogleHomePage(driver)
google_homepage.save_screenshot(os.path.join(directory, "searching.png"))



if __name__ == "__main__":
    test = TestGoogleHomePage()
    test.setup_method(None)
    test.test_search_for_selenium()
    test.teardown_method(None)

