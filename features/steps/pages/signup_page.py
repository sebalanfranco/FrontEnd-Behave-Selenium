from steps.pages.base_page import BasePage

class SignupPage(BasePage):
    By = BasePage.By
    # Locators
    signup_modal = (By.ID, 'signInModal')
    username_input = (By.ID, 'sign-username')
    password_input = (By.ID, 'sign-password')
    # This can be improved
    signup_button = (By.XPATH, '//button[text()="Sign up"]')
    
    def provide_account_information(self, account_information: dict):
        self.find_element(self.username_input).send_keys(account_information['username'])
        self.find_element(self.password_input).send_keys(account_information['password'])
        self.find_child_element(self.signup_modal, self.signup_button).click()
