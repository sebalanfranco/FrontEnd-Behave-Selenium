from steps.pages.base_page import BasePage

class WrapperPage(BasePage):
    By = BasePage.By
    # Locators
    login = (By.ID, 'login2')
    user_welcome = (By.ID, 'nameofuser')
    
    def click_menu_option(self, option: str):
        locator = {
            'login': self.login
        }[option]

        self.find_element(locator).click()

    def get_welcome_message(self):
        self.wait_for_visibility_of_element(self.user_welcome)
        return self.find_element(self.user_welcome).text