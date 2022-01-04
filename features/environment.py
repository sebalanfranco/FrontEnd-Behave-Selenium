from behave import fixture, use_fixture
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# Pages
from steps.pages.base_page import BasePage
from steps.pages.login_page import LoginPage
from steps.pages.wrapper_page import WrapperPage
from steps.pages.signup_page import SignupPage
from steps.pages.product_store_page import ProductStorePage
from steps.pages.cart_page import CartPage
# Utils
from steps.utils.person import Person, RandomPerson
from steps.utils.folder_manager import create_folder

@fixture
def set_webdriver(context):
    # Fixture set up
    context.webdriver = webdriver.Chrome(ChromeDriverManager().install())
    yield context.webdriver
    # Fixture clean up 
    context.webdriver.quit()

@fixture
def save_screenshot(context, filename):
    # Create screenshot name
    context.webdriver.save_screenshot(filename)

def before_all(context):
    # Set up webdriver
    use_fixture(set_webdriver, context)
    context.base_page = BasePage(context.webdriver)
    context.login_page = LoginPage(context.webdriver)
    context.wrapper_page = WrapperPage(context.webdriver)
    context.signup_page = SignupPage(context.webdriver)
    context.product_store_page = ProductStorePage(context.webdriver)
    context.cart_page = CartPage(context.webdriver)
    # Create report folder if doesn't exist
    create_folder(context.config.userdata['report_folder'])

def before_scenario(context, scenario):
    # Set up scenario data
    context.dataset = {
        'user': Person(),
        'random_user': RandomPerson()
    }

def after_scenario(context, scenario):
    # Take screenshot if scenario fails
    if scenario.status == 'failed' and context.config.userdata['screenshot_enabled']:
        create_folder(context.config.userdata['screenshot_folder'])
        filename = f'%s/%s.png' % (context.config.userdata['screenshot_folder'], scenario.name)
        use_fixture(save_screenshot, context, filename)
