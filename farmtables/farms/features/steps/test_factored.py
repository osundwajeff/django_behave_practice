from behave import given, when, then, use_step_matcher
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# uses regex to match
use_step_matcher("re")

# global variables
firefox_options = Options()
#firefox_options.add_argument("--headless")


@given("user is on homepage")
def step_user_is_on_homepage(context):
    context.selenium = webdriver.Firefox(options=firefox_options)
    # homepage
    context.selenium.get(f"http://127.0.0.1:8000/")


@when("user clicks on 'Admin Page'")
def step_user_clicks_on_admin_page(context):
    # navigate to admin login page
    context.selenium.find_element(By.LINK_TEXT, 'Admin Page').click()


@then("user is on the 'Admin Log in page'")
def step_user_is_on_admin_page(context):
    # Assert that the title matches the expected title
    expected_title = "Log in | Django site admin"
    assert context.selenium.title == expected_title


@then("user fills data and clicks on 'Log in'")
def step_clicks_on_login(context):
    # fill in login information
    username = context.selenium.find_element(By.ID, 'id_username')
    username.send_keys("jeff")
    password = context.selenium.find_element(By.ID, 'id_password')
    password.send_keys("jeff123")

    # locate login button and click on it
    context.selenium.find_element(By.XPATH, '//input[@value="Log in"]').click()


@then("page is the 'Admin page'")
def step_page_is_admin_page(context):
    # Assert that the title matches the expected title
    expected_title = "Site administration | Django site admin"
    assert context.selenium.title == expected_title


@then("user returns to the homepage")
def step_user_is_on_homepage(context):
    # locate login button and click on it
    context.selenium.find_element(By.LINK_TEXT, 'VIEW SITE').click()

    # Assert that the title matches the expected title
    expected_title = "Home"
    assert context.selenium.title == expected_title


@then("user clicks on the 'Point of Interest' link")
def step_clicks_on_poi(context):
    context.selenium.find_element(By.LINK_TEXT, 'Point of Interest').click()


@then("page is the 'point_of_interest' page")
def step_page_is_poi(context):
    # Assert that the title matches the expected title
    expected_title = "Point of Interests"
    assert context.selenium.title == expected_title
    # Close the browser window
    context.selenium.quit()
