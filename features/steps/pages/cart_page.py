from steps.pages.base_page import BasePage, By

class CartPage(BasePage):
    # Locators
    products_container = (By.ID, 'tbodyid')
    product_row = (By.CSS_SELECTOR, 'tr[class="success"]')
    order_modal = (By.ID, 'orderModal')
    order_name_input = (By.ID, 'name')
    order_country_input = (By.ID, 'country')
    order_city_input = (By.ID, 'city')
    order_card_input = (By.ID, 'card')
    order_month_input = (By.ID, 'month')
    order_year_input = (By.ID, 'year')
    purchase_confirmation_message = (By.CSS_SELECTOR, '.sweet-alert h2')
    # This can be improved
    delete_product_link = (By.XPATH, '//a[text()="Delete"]')
    place_order_button = (By.XPATH, '//button[text()="Place Order"]')
    purchase_order_button = (By.XPATH, '//button[text()="Purchase"]')
 
    def get_product_information_by_position(self, position: int):
        return self.get_product_by_position(position).text

    def remove_product_by_position(self, position: int):
        return self.find_child_elements(self.products_container, self.delete_product_link)[position - 1].click()

    def get_products_quantity(self):
        return len(self.find_child_elements(self.products_container, self.product_row))

    def get_product_by_position(self, position: int):
        return self.find_child_elements(self.products_container, self.product_row)[position - 1]

    def get_purchase_confirmation_message(self):
        return self.find_element(self.purchase_confirmation_message).text

    def place_order(self):
        self.find_element(self.place_order_button).click()

    def purchase_order(self, billing_information: dict):
        self.find_child_element(self.order_modal, self.order_name_input).send_keys(billing_information['name'])
        self.find_child_element(self.order_modal, self.order_country_input).send_keys(billing_information['country'])
        self.find_child_element(self.order_modal, self.order_city_input).send_keys(billing_information['city'])
        self.find_child_element(self.order_modal, self.order_card_input).send_keys(billing_information['card'])
        self.find_child_element(self.order_modal, self.order_month_input).send_keys(billing_information['month'])
        self.find_child_element(self.order_modal, self.order_year_input).send_keys(billing_information['year'])
        self.find_element(self.purchase_order_button).click()