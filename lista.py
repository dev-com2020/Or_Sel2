import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://crossbrowsertesting.github.io/selenium_example_page.html")

element = driver.find_element(By.ID, "dropdown")

select_obj = Select(element)
# select_obj.select_by_value("option3")
# select_obj.select_by_visible_text("Option 2")
# select_obj.select_by_index(0)
time.sleep(3)
driver.find_element(By.ID, "submitbtn").click()
all = select_obj.all_selected_options # multiselect!
print(all)
