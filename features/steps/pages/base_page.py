from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    Keys = Keys
    By = By

    def __init__(self, webdriver):
        self.browser = webdriver
        self.browser.implicitly_wait(10)

    def visit(self, url):
        self.browser.get(url)

    def find_element(self, locator):
        return self.browser.find_element(*locator)

    def find_child_element(self, parent_locator, child_locator):
        return self.browser.find_element(*parent_locator).find_element(*child_locator)

    # Explicit waits
    def wait_for_visibility_of_element(self, locator, timeout = 5):
        wait = WebDriverWait(self.browser, timeout)
        return wait.until(EC.visibility_of_element_located(locator))
