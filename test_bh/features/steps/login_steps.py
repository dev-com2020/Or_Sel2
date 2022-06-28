import time

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium import webdriver

password = 'boleklolek123'
driver = webdriver.Chrome()
driver.implicitly_wait(2)

@given('user is on Poczta Onet website')
def step_start_page(context):
    driver.get('https://poczta.onet.pl')
    time.sleep(3)

@when('user fills in the Sign In form {login} and {pass} and submits it')
def step_set_login_in(context, login):
    driver.find_element(By.XPATH, '//*[@id="rasp_cmp"]/div/div[6]/button[2]/span').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(login)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[1]/div/div[1]/div/div[3]/form/div[2]/div').click()


@then('User can see email list')
def step_valid_login(context):
    driver.save_screenshot('behave_test.png')
    time.sleep(3)
