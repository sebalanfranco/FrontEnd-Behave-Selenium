from behave import given

# GIVEN steps
@given('I navigate to Demoblaze site')
def step_impl(context):
    context.base_page.visit(context.config.userdata['base_url'])
