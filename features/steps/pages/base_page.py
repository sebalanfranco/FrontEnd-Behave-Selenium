from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import ElementNotVisibleException

class BasePage:
    """Base page object conains the logic to use Selenium webdriver and interact with web elements."""
    Keys = Keys
    By = By

    def __init__(self, webdriver):
        # Set browser with webdriver instance
        self.browser = webdriver
        # Incrementing implicit wait
        self.browser.implicitly_wait(10)

    
    def visit(self, url):
        """
        Visit the passed url

        Parameters:
        url (str): Url to visit
        """
        self.browser.get(url)

    def find_element(self, locator):
        """
        Find element by locator

        Parameters:
        locator (tuple): element locator

        Returns:
        WebElement
        """
        return self.browser.find_element(*locator)

    def find_elements(self, locator):
        """
        Find elements by locator

        Parameters:
        locator (tuple): elements locator

        Returns:
        list
        """
        return self.browser.find_elements(*locator)

    def find_child_element(self, parent_locator, child_locator):
        """
        Find child element within the parent

        Parameters:
        parent_locator (tuple): parent element locator
        child_locator (tuple): child element locator

        Returns:
        WebElement
        """
        return self.browser.find_element(*parent_locator).find_element(*child_locator)

    def find_child_elements(self, parent_locator, child_locator):
        """
        Find child elements within the parent

        Parameters:
        parent_locator (tuple): parent element locator
        child_locator (tuple): child elements locator

        Returns:
        list
        """
        return self.browser.find_element(*parent_locator).find_elements(*child_locator)

    def get_alert_message(self):
        """
        Get message from browser alert

        Returns:
        str
        """
        self.wait_for_alert()
        
        return Alert(self.browser).text

    def accept_alert(self):
        """
        Accept browser alert
        """
        self.wait_for_alert()
        Alert(self.browser).accept()

    # Explicit waits
    def wait_for_visibility_of_element(self, locator, timeout = 5):
        """
        Wait for element to be visible

        Parameters:
        locator (tuple): element locator
        timeout (int): wait timeout (default = 5)
        """
        wait = WebDriverWait(self.browser, timeout)
        wait.until(EC.visibility_of_element_located(locator))

    def wait_for_alert(self, timeout = 5):
        """
        Wait for browser alert to be present

        Parameters:
        timeout (int): wait timeout (default = 5)
        """
        wait = WebDriverWait(self.browser, timeout)
        wait.until(EC.alert_is_present())

    def wait_for_element_to_disappear(self, element, timeout = 5):
        """
        Wait for element to be not present

        Parameters:
        element (WebElement): element to disappear
        timeout (int): wait timeout (default = 5)
        """
        wait = WebDriverWait(self.browser, timeout, ignored_exceptions = (ElementNotVisibleException))
        wait.until_not(lambda e: element.is_displayed())
