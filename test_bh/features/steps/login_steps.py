import time

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(2)

@given('user is on automationpractice website')
def step_start_page(context):
    driver.get('https://automationpractice.com')
    time.sleep(5)

@when('user fills in the search form {search} and submits it')
def step_set_login_in(context, search):

    driver.find_element(By.XPATH, '//*[@id="search_query_top"]').send_keys(search)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="searchbox"]/button').click()


@then('User can see search result, and take a screenshot with {num} number')
def step_valid_login(context, num):
    driver.save_screenshot(f"test_behave{num}.png")
    time.sleep(2)
