from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

vService = Service(executable_path="msedgedriver.exe")
vEdge = webdriver.Edge(service=vService)
vEdge.maximize_window()
vEdge.get("https://paczkadoukrainy.pl/")

vEdge.find_element(By.NAME, "parcelWeight").send_keys("20")
vEdge.find_element(By.CSS_SELECTOR, ".btn:nth-child(5)").click()
vEdge.execute_script("window.scrollBy(0,750)")
vEdge.find_element(By.XPATH, '//*[@id="offerListCalc"]/div[1]/div[6]/div/div/div[2]/div/div[3]/button').click()

vEdge.save_screenshot("PdU_GLS.png")
# vEdge.quit()
