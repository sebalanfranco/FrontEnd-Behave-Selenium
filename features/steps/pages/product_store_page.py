from steps.pages.base_page import BasePage, By
from selenium.common.exceptions import StaleElementReferenceException

class ProductStorePage(BasePage):
    # Locators
    products_container = (By.ID, 'tbodyid')
    product_card = (By.CLASS_NAME, 'card')
    product_card_title = (By.CLASS_NAME, 'card-title')
    product_name = (By.CLASS_NAME, 'name')
    products = (By.CSS_SELECTOR, '#tbodyid .card')
    # This can be improved
    add_to_cart = (By.XPATH, '//a[text()="Add to cart"]')
    
    # TODO: improve and move method to base page
    def open_product_by_position(self, position: int):
        for i in range(10):
            try:
                self._get_product_by_position(position).click()
                break
            except StaleElementReferenceException:
                continue

    def get_product_information_by_position(self, position: int):
        product_card = self._get_product_by_position(position)
        information = {
            # TODO: improve BasePage.find_child_element() to support this case
            'name': self._get_product_by_position(position).find_element(*self.product_card_title).text
        }

        return information

    def get_product_name(self):
        return self.find_element(self.product_name).text

    def add_product_to_cart(self):
        self.find_element(self.add_to_cart).click()

    def _get_product_by_position(self, position: int):
        return self.find_child_elements(self.products_container, self.product_card)[position - 1]

    def wait_for_products(self):
        self.wait_for_visibility_of_element(self.products)
