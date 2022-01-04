from steps.pages.base_page import BasePage, By

class LoginPage(BasePage):
    # Locators
    login_modal = (By.ID, 'logInModal')
    username_input = (By.ID, 'loginusername')
    password_input = (By.ID, 'loginpassword')
    # This can be improved
    login_button = (By.XPATH, '//button[text()="Log in"]')
    
    def provide_credentials(self, credentials: dict):
        self.find_element(self.username_input).send_keys(credentials['username'])
        self.find_element(self.password_input).send_keys(credentials['password'])
        self.find_child_element(self.login_modal, self.login_button).click()
