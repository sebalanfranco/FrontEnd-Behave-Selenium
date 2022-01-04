from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

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

    def get_alert_message(self):
        self.wait_for_alert()
        
        return Alert(self.browser).text

    def accept_alert(self):
        self.wait_for_alert()
        Alert(self.browser).accept()

    # Explicit waits
    def wait_for_visibility_of_element(self, locator, timeout = 5):
        wait = WebDriverWait(self.browser, timeout)
        
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_for_alert(self, timeout = 5):
        wait = WebDriverWait(self.browser, timeout)
        
        return wait.until(EC.alert_is_present())
