from selenium import webdriver
from selenium.webdriver.common.by import By



class TestPaczkatest():
    def setup_method(self, method):
        self.driver = webdriver.Edge()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_paczkatest(self):
        self.driver.get("https://paczkadoukrainy.pl/")
        self.driver.set_window_size(1936, 1048)
        self.driver.find_element(By.NAME, "parcelWeight").click()
        self.driver.find_element(By.NAME, "parcelWeight").send_keys("10")
        self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(5)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(6) .btn").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.close()