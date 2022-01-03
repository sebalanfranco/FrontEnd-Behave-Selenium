from behave import given

@given('I navigate to Demoblaze site')
def step_impl(context):
    context.base_page.visit(context.config.userdata['base_url'])

@then('I should be logged in')
def step_impl(context):
    text = context.wrapper_page.get_welcome_message()
    expected_text = f'Welcome %s' % context.dataset['user'].username 
    
    assert text == expected_text, (f'Expected %s to equal %s' % (text, expected_text))