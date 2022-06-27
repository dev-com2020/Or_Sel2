import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Test1111():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_1111(self):
        self.driver.get("https://www.google.pl/")
        self.driver.set_window_size(945, 1012)
        self.driver.find_element(By.CSS_SELECTOR, "#L2AGLb > .QS5gu").click()
        self.driver.find_element(By.NAME, "q").click()
        self.driver.find_element(By.NAME, "q").send_keys("bilety do kina")
        self.driver.find_element(By.NAME, "q").send_keys(Keys.ARROW_DOWN)
        select_el = self.driver.find_element(By.CLASS_NAME, "G43f7e")
        select_obj = Select(select_el)
        select_obj.select_by_index(1)
        time.sleep(2)
        self.driver.save_screenshot("testXXX.png")

        # try:
        #     WebDriverWait(self.driver, 5).until(
        #         EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "bilety do kina"))
        #     )
        #     self.driver.find_element(By.PARTIAL_LINK_TEXT, "bilety do kina").screenshot("zad2.jpg")
        # finally:
        #     # else quit
        #     self.driver.quit()

        # time.sleep(3)
        # self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
        # time.sleep(3)
        # self.driver.close()
