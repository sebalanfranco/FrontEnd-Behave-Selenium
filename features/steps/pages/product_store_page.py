from steps.pages.base_page import BasePage

class ProductStorePage(BasePage):
    By = BasePage.By
    # Locators
    products_container = (By.ID, 'tbodyid')
    product_card = (By.CLASS_NAME, 'card')
    product_card_title = (By.CLASS_NAME, 'card-title')
    product_name = (By.CLASS_NAME, 'name')
    # This can be improved
    add_to_cart = (By.XPATH, '//a[text()="Add to cart"]')
    
    def open_product_by_position(self, position: int):
        self.wait_for_visibility_of_element(self.product_card_title)
        self._get_product_by_position(position).click()

    def get_product_information_by_position(self, position: int):
        product_card = self._get_product_by_position(position)
        information = {
            'name': self._get_product_name_by_position(position)
        }

        return information

    def get_product_name(self):
        return self.find_element(self.product_name).text

    def add_product_to_cart(self):
        self.find_element(self.add_to_cart).click()

    def _get_product_by_position(self, position: int):
        return self.find_child_elements(self.products_container, self.product_card)[position - 1]

    def _get_product_name_by_position(self, position: int):
        # TODO: improve BasePage.find_child_element() to support this case
        return self._get_product_by_position(position).find_element(*self.product_card_title).text
