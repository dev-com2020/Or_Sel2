import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

service = Service(executable_path="msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.maximize_window()
driver.get("https://paczkadoukrainy.pl/pl/homepage")

# Zamkniecie info coockie
driver.find_element(By.CLASS_NAME, "eupopup-closebutton").click()

driver.find_element(By.PARTIAL_LINK_TEXT, "NADAJ").click()
time.sleep(5)

#  GLS
driver.find_element(By.CSS_SELECTOR, ".row:nth-child(4) .btn").click()

# Dane do formularz adresowego
nadawca = "Alojzy Alojz"
nad_kod = "31-205"
nad_miejsc = "Kraków"
nad_ulica = "Uliczna"
nad_tel = "123456678"
nad_email = "a@asz.pl"
adresat = "Piotr Wala"
adr_kod = "20543"
adr_miejsc = "Kijów"
adr_ulica = "Kijowska"
adr_tel = "876565432"
adr_email = "gd@asz.uk"

# Wypelnienie formularza
driver.find_element(By.NAME, "senderAddressName").send_keys(nadawca)
driver.find_element(By.NAME, "senderPostalCode").send_keys(nad_kod)
driver.find_element(By.NAME, "senderAddressCity").send_keys(nad_miejsc)
driver.find_element(By.NAME, "senderAddressStreet").send_keys(nad_ulica)
driver.find_element(By.NAME, "senderAddressHouse").send_keys("23")
driver.find_element(By.NAME, "senderAddressPhone").send_keys(nad_tel)
driver.find_element(By.NAME, "senderAddressEmail").send_keys(nad_email)
driver.find_element(By.NAME, "recipentAddressName").send_keys(adresat)
driver.find_element(By.NAME, "recipientPostalCode").send_keys(adr_kod)
driver.find_element(By.NAME, "recipentAddressCity").send_keys(adr_miejsc)
driver.find_element(By.NAME, "recipentAddressStreet").send_keys(adr_ulica)
driver.find_element(By.NAME, "recipentAddressBuildingNumber").send_keys("13")
driver.find_element(By.NAME, "recipentPhone").send_keys(adr_tel)
driver.find_element(By.NAME, "recipentAddressEmail").send_keys(adr_email)
driver.save_screenshot("wypelniona_formatka_adresowa.png")

# Dane do formularza paczki
p1_co = "zabawka"
p1_ile = "1"
p1_waga = "4"
p1_war = "45"

# Wypelnienie formularza paczki
driver.find_element(By.NAME, "parcelItemDescription-0").send_keys(p1_co)
driver.find_element(By.NAME, "parcelItemQuantity-0").send_keys(p1_ile)
driver.find_element(By.NAME, "parcelItemWeight-0").send_keys(p1_waga)
driver.find_element(By.NAME, "parcelItemValueClientCurrency-0").send_keys(p1_war)
driver.find_element(By.NAME, "parcelWeight2").send_keys(p1_waga)
driver.find_element(By.CSS_SELECTOR, ".mb-3:nth-child(2) .custom-control-label").click()
driver.find_element(By.CSS_SELECTOR, ".mb-3:nth-child(3) > .col-12 .custom-control-label").click()
driver.find_element(By.CSS_SELECTOR, ".row:nth-child(4) .custom-control-label").click()
driver.find_element(By.CSS_SELECTOR, ".row:nth-child(5) .custom-control-label").click()

driver.save_screenshot("wypelniona_formatka_paczki.png")
driver.find_element(By.ID, "btn_next_step").click()
time.sleep(5)
driver.save_screenshot("podsumowanie.png")

# time.sleep(10)
driver.close()