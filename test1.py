import time
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


username = "devcomsotfhouse"
access_key = "I3yG5tdQlriH8Iyik2zY2VsgGCYjJ6FnAQuVyZeqcUOPBVvEiz"

def get_browser(caps):
	return webdriver.Remote(command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key),desired_capabilities=caps)

# You can configure your test capabilities here

browsers = [{
  "build": 'PyunitTest sample build', # Change your build name here
  "name": 'Py-unittest1', # Change your test name here
  "platform": 'Windows 10', # Change your OS version here
  "browserName": 'MicrosoftEdge', # Change your browser here
  "version": '98.0', # Change your browser version here
  "resolution": '1920x1080' # Change your resolution here
},
{
  "build": 'PyunitTest sample build', # Change your build name here
  "name": 'Py-unittest2', # Change your test name here
  "platform": 'Windows 10', # Change your OS version here
  "browserName": 'Chrome', # Change your browser here
  "version": '92.0', # Change your browser version here
  "resolution": '1024x768' # Change your resolution here
},
{
  "build": 'PyunitTest sample build', # Change your build name here
  "name": 'Py-unittest3', # Change your test name here
  "platform": 'Windows 10', # Change your OS version here
  "browserName": 'Firefox', # Change your browser here
  "version": '98.0', # Change your browser version here
  "resolution": '1024x768' # Change your resolution here
}]
browsers_waiting = []
def get_browser_and_wait(browser_data):
    driver = get_browser(browser_data)

    driver.maximize_window()
    driver.get("https://www.google.pl")
    driver.find_element(By.XPATH, '//*[@id="L2AGLb"]/div').click()
    time.sleep(5)
    print("---Teraz klikam w pole szukaj---")
    driver.find_element(By.NAME, "q").click()
    driver.find_element(By.NAME, "q").send_keys("makowiec")
    driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    time.sleep(5)
    driver.find_element(By.PARTIAL_LINK_TEXT, "Kwestia").click()
    time.sleep(5)
    driver.save_screenshot("wynik.png")
    driver.quit()
    input("Wciśnij ENTER aby zakończyć...")

thread_list = []
for i, browser in enumerate(browsers):
    t = Thread(target=get_browser_and_wait, args=[browser])
    thread_list.append(t)
    t.start()

for t in thread_list:
    t.join()
