from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By

username = "devcomsotfhouse"
access_key = "I3yG5tdQlriH8Iyik2zY2VsgGCYjJ6FnAQuVyZeqcUOPBVvEiz"


def get_browser(caps):
    return webdriver.Remote(
        command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key),
        desired_capabilities=caps
    )


browsers = [{
    "build": 'PyunitTest sample build',  # Change your build name here
    "name": 'Py-unittest1',  # Change your test name here
    "platform": 'Windows 11',  # Change your OS version here
    "browserName": 'Opera',  # Change your browser here
    "version": '80.0',  # Change your browser version here
    "resolution": '1920x1080'  # Change your resolution here
},
    {
        "build": 'PyunitTest sample build',  # Change your build name here
        "name": 'Py-unittest2',  # Change your test name here
        "platform": 'Windows 8.1',  # Change your OS version here
        "browserName": 'MicrosoftEdge',  # Change your browser here
        "version": '93.0',  # Change your browser version here
        "resolution": '1280x800'  # Change your resolution here
    },
    {
        "build": 'PyunitTest sample build',  # Change your build name here
        "name": 'Py-unittest3',  # Change your test name here
        "platform": 'Windows 7',  # Change your OS version here
        "browserName": 'Internet Explorer',  # Change your browser here
        "version": '10.0',  # Change your browser version here
        "resolution": '1366x768'  # Change your resolution here
    }]
browsers_waiting = []


def get_browser_and_wait(browser_data):
    driver = get_browser(browser_data)
    driver.get("https://paczkadoukrainy.pl/")
    driver.maximize_window()
    driver.find_element(By.NAME, "parcelWeight").click()
    driver.find_element(By.NAME, "parcelWeight").send_keys("10")
    driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(5)").click()
    driver.execute_script("window.scrollTo(0,750)")
    driver.find_element(By.XPATH, '//*[@id="offerListCalc"]/div[1]/div[6]/div/div/div[2]/div/div[3]/button').click()

    driver.close()


thread_list = []
for i, browser in enumerate(browsers):
	t = Thread(target=get_browser_and_wait, args=[browser])
	thread_list.append(t)
	t.start()

for t in thread_list:
	t.join()
