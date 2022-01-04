from behave import given, when

#GIVEN steps
@given('I am in product catalog')
def step_impl(context):
    context.wrapper_page.click_menu_option('home')

# WHEN steps
@when('I open the {modal} modal')
def step_impl(context, modal):    
    context.wrapper_page.click_menu_option(modal)

@when('I open the cart')
def step_impl(context):    
    context.wrapper_page.click_menu_option('cart')    
