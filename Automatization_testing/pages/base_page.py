from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement


class BasePage():

    def __init__(self, browser: WebDriver, url):
        self.browser = browser
        self.url = url
        self.wait = WebDriverWait(self.browser, 10)

    def open(self):
        self.browser.get(self.url)

    def is_visible(self, locator) -> WebElement:
        return self.wait.until(ec.visibility_of_element_located(locator))
