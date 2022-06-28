import time
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome()

driver.get("https://www.google.pl/")
driver.set_window_size(1597, 1012)
driver.find_element(By.CSS_SELECTOR, "#L2AGLb > .QS5gu").click()
driver.find_element(By.NAME, "q").click()
driver.find_element(By.NAME, "q").send_keys("bilety do kina")
time.sleep(3)
driver.find_element(By.NAME, "q").send_keys(Keys.ARROW_DOWN)
page_source = driver.page_source

soup = BeautifulSoup(page_source, 'lxml')
reviews = []
reviews_selector = soup.find_all('li', class_='sbct')
for review_selector in reviews_selector:
    review_li = review_selector.findNext('li')
    if review_li is None:
        review_li = review_selector.findNext('li')
    review = review_li.findNext('span').get_text()
    review = review.strip()
    reviews.append(review)
print(reviews)
