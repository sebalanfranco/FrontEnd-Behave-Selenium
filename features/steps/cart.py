from behave import when, then

# WHEN steps
@when('I remove the first product')
def step_impl(context):
    context.dataset['products_quantity'] = context.cart_page.get_products_quantity()
    element_to_remove = context.cart_page.get_product_by_position(1)
    context.cart_page.remove_product_by_position(1)
    context.base_page.wait_for_element_to_disappear(element_to_remove)

@when('I place the order')
def step_impl(context):
    context.dataset['products_total'] = context.cart_page.get_products_total()
    context.cart_page.place_order()

@when('I purchase the order')
def step_impl(context):
    context.execute_steps('''
        When I place the order
    ''')
    billing_information = {
        'name': context.dataset['user'].name,
        'country': context.dataset['user'].address['country'],
        'city': context.dataset['user'].address['city'],
        'card': context.dataset['user'].credit_card['number'],
        'month': context.dataset['user'].credit_card['expiration_month'],
        'year': context.dataset['user'].credit_card['expiration_year']
    }
    context.cart_page.purchase_order(billing_information)

# THEN steps
@then('I should see the product')
def step_impl(context):
    text = context.cart_page.get_product_information_by_position(1)
    expected_text = context.dataset['selected_product']['name']
    
    assert expected_text in text, (f'Expected %s to contain %s' % (text, expected_text))

@then('I should see that a product was removed')
def step_impl(context):
    value = context.cart_page.get_products_quantity()
    expected_value = context.dataset['products_quantity'] - 1
    
    assert expected_value == value, (f'Expected %s to equal %s' % (value, expected_value))

@then('I should see that the purchase is confirmed')
def step_impl(context):
    text = context.cart_page.get_purchase_confirmation_message()
    expected_text = 'Thank you for your purchase!'
    
    assert expected_text == text, (f'Expected %s to equal %s' % (text, expected_text))

@then('I should see that the order is ready')
def step_impl(context):
    text = context.cart_page.get_order_total()
    expected_text = context.dataset['products_total']
    
    assert expected_text == text, (f'Expected %s to equal %s' % (text, expected_text))
