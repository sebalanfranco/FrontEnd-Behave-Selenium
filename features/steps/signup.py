from behave import when

# WHEN steps
@when('I provide my account information')
def step_impl(context):
    account_information = {
        'username': context.dataset['random_user'].username,
        'password': context.dataset['random_user'].password
    }
    context.signup_page.provide_account_information(account_information)

@when('I provide an existent account information')
def step_impl(context):
    account_information = {
        'username': context.dataset['user'].username,
        'password': context.dataset['user'].password
    }
    context.signup_page.provide_account_information(account_information)

@when('I enter a new {data}')
def step_impl(context, data):
    account_information = {
        'username': context.dataset['random_user'].username if data == 'username' else '',
        'password': context.dataset['random_user'].password if data == 'password' else ''
    }
    context.signup_page.provide_account_information(account_information)

# THEN steps
@then('I should see the "{message}" alert message')
def step_impl(context, message):
    text = context.base_page.get_alert_message()
    # Accepting alert for stability
    context.base_page.accept_alert()
    expected_text = message
    
    assert text == expected_text, (f'Expected %s to equal %s' % (text, expected_text))
