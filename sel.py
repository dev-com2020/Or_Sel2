# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# service = Service(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
# driver.get("https://onet.pl")

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://selenium.dev")
driver.quit()

