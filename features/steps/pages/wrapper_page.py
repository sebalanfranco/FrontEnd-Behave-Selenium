from steps.pages.base_page import BasePage, By

class WrapperPage(BasePage):
    # Locators
    login = (By.ID, 'login2')
    sign_up = (By.ID, 'signin2')
    user_welcome = (By.ID, 'nameofuser')
    # This can be improved
    cart = (By.XPATH, '//a[text()="Cart"]')

    def click_menu_option(self, option: str):
        locator = {
            'login': self.login,
            'sign up': self.sign_up,
            'cart': self.cart
        }[option]

        self.find_element(locator).click()

    def get_welcome_message(self):
        self.wait_for_visibility_of_element(self.user_welcome)
        return self.find_element(self.user_welcome).text