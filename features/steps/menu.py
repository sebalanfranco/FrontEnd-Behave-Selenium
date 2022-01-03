from behave import when

@when('I open the login modal')
def step_impl(context):    
    context.wrapper_page.click_menu_option('login')
