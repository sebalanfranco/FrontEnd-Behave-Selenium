from behave import when

# WHEN steps
@when('I provide my credentials')
def step_impl(context):
    credentials = {
        'username': context.dataset['user'].username,
        'password': context.dataset['user'].password
    }
    context.login_page.provide_credentials(credentials)

@when('I provide a non-existent username')
def step_impl(context):
    account_information = {
        'username': context.dataset['random_user'].username,
        'password': context.dataset['user'].password
    }
    context.login_page.provide_credentials(account_information)

@when('I provide a wrong password')
def step_impl(context):
    account_information = {
        'username': context.dataset['user'].username,
        'password': f'%s%s' % (context.dataset['user'].password, 'wrong')
    }
    context.login_page.provide_credentials(account_information)

# THEN steps
@then('I should be successfully logged in')
def step_impl(context):
    text = context.wrapper_page.get_welcome_message()
    expected_text = f'Welcome %s' % context.dataset['user'].username 
    
    assert text == expected_text, (f'Expected %s to equal %s' % (text, expected_text))