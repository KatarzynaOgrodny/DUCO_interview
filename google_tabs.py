from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class GoogleHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.NAME, "q")
        self.accept_button = (By.XPATH, "//*[text()='Accept all']")

    def load(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element(*self.accept_button).click()

    def search(self, query):
        search_box = self.driver.find_element(*self.search_box)
        search_box.send_keys(query)
        search_box.submit()

    def click_videos_tab(self):
        videos_tab = self.driver.find_element(By.XPATH, "//a[contains(text(),'Videos')]")
        videos_tab.click()
        return GoogleVideosPage(self.driver)

    def click_images_tab(self):
        images_tab = self.driver.find_element(By.XPATH, "//a[contains(text(),'Images')]")
        images_tab.click()
        return GoogleImagesPage(self.driver)

    def click_shopping_tab(self):
        shopping_tab = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Shopping']"))
        )
        shopping_tab.click()
        return GoogleShoppingPage(self.driver)


class GoogleVideosPage:
    def __init__(self, driver):
        self.driver = driver

    def is_loaded(self):
        return EC.presence_of_element_located((By.ID, "search"))

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)


class GoogleImagesPage:
    def __init__(self, driver):
        self.driver = driver

    def is_loaded(self):
        return EC.presence_of_element_located((By.ID, "search"))

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)


class GoogleShoppingPage:
    def __init__(self, driver):
        self.driver = driver

    def is_loaded(self):
        return EC.presence_of_element_located((By.XPATH, "//div[@class='N6sL8d']"))

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)


directory = "screenshots_tab"
if not os.path.exists(directory):
    os.makedirs(directory)


driver = webdriver.Chrome()
google_homepage = GoogleHomePage(driver)
google_homepage.load()
google_homepage.search("selenium automation testing")
google_videos_page = google_homepage.click_videos_tab()
google_videos_page.is_loaded()
google_videos_page.take_screenshot(os.path.join(directory, "video_results.png"))
google_images_page = google_homepage.click_images_tab()
google_images_page.is_loaded()
google_images_page.take_screenshot(os.path.join(directory, "image_results.png"))
google_shopping_page = google_homepage.click_shopping_tab()
google_shopping_page.is_loaded()
google_shopping_page.take_screenshot(os.path.join(directory, "shopping_tab.png"))
driver.quit()
