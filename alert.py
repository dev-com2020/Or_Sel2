import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By



def okienko():
    driver.find_element(By.LINK_TEXT, "Kliknij, aby wyświetlić okienko prompt").click()
    time.sleep(3)
    alert = Alert(driver)
    text = alert.text
    alert.send_keys("Tutaj wpisuje coś....")
    print(text)
    alert.accept()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("D:\\projekty_\\1\\alerty.html")
okienko()

# if zmienna == "stop":
#     okienko()

# alert.dismiss()

# element = wait.until(expected_conditions.element_to_be_clickable(By.XPATH, "//div"))
# wait = WebDriverWait(driver, 9, poll_frequency=2, ignored_exceptions=[ElementNotVisibleException])

