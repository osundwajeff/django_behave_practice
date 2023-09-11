from behave import given, when, then, use_step_matcher
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# uses regex to match
use_step_matcher("re")

# global variables
firefox_options = Options()
firefox_options.add_argument("--headless")


@given("user is on 'Admin Log in page'")
def step_iml(context):
    context.selenium = webdriver.Firefox(options=firefox_options)
    # login to admin panel
    context.selenium.get(f"http://127.0.0.1:8000/admin/")


@when("user clicks on 'Log in'")
def step_iml(context):
    # fill in login information
    username = context.selenium.find_element(By.ID, 'id_username')
    username.send_keys("jeff")
    password = context.selenium.find_element(By.ID, 'id_password')
    password.send_keys("jeff123")

    # locate login button and click on it
    context.selenium.find_element(By.XPATH, '//input[@value="Log in"]').click()


@then("page is 'Admin page'")
def step_iml(context):
    # Assert that the title matches the expected title
    expected_title = "Site administration | Django site admin"
    assert context.selenium.title == expected_title