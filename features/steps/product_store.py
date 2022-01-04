from behave import given, when, then

# GIVEN steps
@given('I added a product to the cart')
def step_impl(context):
    context.execute_steps('''
        When I open the first product
        And I add the product to the cart
        Then I should see the "Product added." alert message
    ''')

# WHEN steps
@when('I open the first product')
def step_impl(context):
    # This can be improved using a data driven approach
    context.dataset['selected_product'] = context.product_store_page.get_product_information_by_position(1)
    context.product_store_page.open_product_by_position(1)

@when('I add the product to the cart')
def step_impl(context):
    # This can be improved using a data driven approach
    context.product_store_page.add_product_to_cart()

# THEN steps
@then('I should see the product information')
def step_impl(context):
    text = context.product_store_page.get_product_name()
    expected_text = context.dataset['selected_product']['name']
    
    assert text == expected_text, (f'Expected %s to equal %s' % (text, expected_text))
