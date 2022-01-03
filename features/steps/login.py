from behave import when

@when('I provide my credentials')
def step_impl(context):
    credentials = {
        'username': context.dataset['user'].username,
        'password': context.dataset['user'].password
    }
    context.login_page.provide_credentials(credentials)
