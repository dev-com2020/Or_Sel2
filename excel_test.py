import time
import unittest

import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By



def data_from_excel(path):
    data_list = []
    data = xlrd.open_workbook(path)
    sheet = data.sheet_by_index(0)
    sheet.cell_value(0, 0)

    for i in range(sheet.nrows):
        data_list.append(sheet.cell_value(i, 0))
    return data_list

class Test1(unittest.TestCase):
    driver = webdriver.Chrome()

    def test_email_button(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php?controller=authentication&amp;back=my-account")
        wrong_emails = data_from_excel("wrong_mails.xls")

        for e in wrong_emails:
            email = driver.find_element(By.XPATH, '//*[@id="email_create"]')
            email.send_keys(e)
            login = driver.find_element(By.XPATH, '//*[@id="SubmitCreate"]')
            login.click()
            time.sleep(2)
            self.assertEquals("rgba(241, 51, 64, 1)", email.value_of_css_property("border-bottom-color"))
            email.clear()