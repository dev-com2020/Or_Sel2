import wait as wait
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def okienko():
    driver.find_element(By.LINK_TEXT, "Kliknij, aby wyświetlić okienko prompt").click()
    WebDriverWait(driver,
                  timeout=3,
                  poll_frequency=3,
                  ignored_exceptions=[ElementNotVisibleException]).until(expected_conditions.alert_is_present())
    alert = Alert(driver)
    text = alert.text
    alert.send_keys("Tutaj wpisuje coś....")
    print(text)
    alert.accept()


service = Service(executable_path="msedgedriver.exe")
driver = webdriver.Edge()
driver.maximize_window()
driver.get(r"F:\Or_Sel\alerty.html")
zmienna = driver.find_element(By.NAME, "okno")

if zmienna == "stop":
    okienko()

# alert.dismiss()

element = wait.until(expected_conditions.element_to_be_clickable(By.XPATH, "//div"))
wait = WebDriverWait(driver, 9, poll_frequency=2, ignored_exceptions=[ElementNotVisibleException])

