from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.zomato.com')

# storing the current window handle to get back to dashboard
main_page = driver.current_window_handle

# wait for page to load completely
sleep(5)

# click on the sign in tab
driver.find_element(By.LINK_TEXT, 'Sign up').click()

sleep(5)

# click to log in using google
driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/section[2]/section/div[4]').click()

# changing the handles to access login page
for handle in driver.window_handles:
    if handle != main_page:
        login_page = handle

# change the control to signin page
driver.switch_to.window(login_page)

# user input for email and password
print('Enter email id : ', end='')
email = input().strip()

# enter the email
driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(email)
driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
# enter the password
sleep(3)
print('Enter password : ', end='')
password = input().strip()
driver.find_element(By.XPATH, '//*[@id ="pass"]').send_keys(password)

# click the login button
driver.find_element(By.XPATH, '//*[@id ="u_0_0"]').click()

# change control to main page
driver.switch_to.window(main_page)

sleep(10)
# print user name
name = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/header/div[2]/div/div/div/div/span').text
print('Your user name is : {}'.format(name))

# closing the window
driver.quit()
