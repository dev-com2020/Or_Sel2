import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_2:
    def test(self):
        driver = webdriver.Chrome()
        self.latitude = 54.35292775991906
        self.longitude = 18.651018342356778
        self.accuracy = 100

        driver.maximize_window()
        driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "accuracy": self.accuracy
        })

        driver.get('https://oknoplast.com.pl')
        time.sleep(2)
        driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "Gdzie kupić?").click()
        time.sleep(2)
        location_icon = driver.find_element(By.XPATH, '//*[@id="geoLocation"]')
        location_icon.click()
        time.sleep(3)
