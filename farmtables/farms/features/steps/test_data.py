from behave import given, when, then, use_step_matcher
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# uses regex to match
use_step_matcher("re")

# global variables
firefox_options = Options()
#firefox_options.add_argument("--headless")


@given("the user is on the 'point of interest' page")
def step_user_on_point_of_interest_page(context):
    context.selenium = webdriver.Firefox(options=firefox_options)
    context.selenium.get(f"http://127.0.0.1:8000/create_point_of_interest/")


@when("the user clicks on draw item")
def step_user_clicks_draw(context):
    context.selenium.find_element(By.LINK_TEXT, 'Draw a marker').click()


@then("a form pops-up and user inputs data")
def step_form_pop_up(context):
    # fill in login information
    context.selenium.find_element(By.ID, 'map').click()
    context.selenium.find_element(By.ID, 'addPointForm')
    # point of interest type
    poi_type = context.selenium.find_element(By.ID, 'type')
    poi_type.send_keys("Electric")
    # notes
    notes = context.selenium.find_element(By.ID, 'notes')
    notes.send_keys("jeff")
    # height(m)
    height = context.selenium.find_element(By.ID, 'height_m')
    height.send_keys("2.5")
    # installation date
    installation_date = context.selenium.find_element(By.ID, 'installation_date')
    installation_date.send_keys("2023-09-12")
    # is the date estimated
    is_date_estimated = context.selenium.find_element(By.ID, 'is_date_estimated')
    is_date_estimated.send_keys("True")
    # submit
    context.selenium.find_element(By.ID, 'add_point').click()
    context.selenium.quit()
