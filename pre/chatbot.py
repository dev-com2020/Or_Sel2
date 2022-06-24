from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import random
from selenium.webdriver.common.keys import Keys
import time

chrome = webdriver.Chrome(ChromeDriverManager().install())

chrome.get("https://web.whatsapp.com")
time.sleep(40)

search_box = chrome.find_element(By.CLASS_NAME, "_13NKt")
search_box.send_keys("Ala")
search_box.send_keys(Keys.ENTER)
time.sleep(3)


message_box = chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div')
for i in range(10):
    message_box.send_keys("Hello!!")
    message_box.send_keys(Keys.ENTER)
time.sleep(3)

emoji = [":-)", ";-)", ">_<", ":-(", "^_^"]
message_box = chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div')
for i in range(10):
    message_box.send_keys(random.choice(emoji))
    message_box.send_keys(Keys.ENTER)
time.sleep(3)

attachement_box = chrome.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span')
attachement_box.click()

# !wget 'https://pbs.twimg.com/profile_images/1091974962804514817/lhsJS84G_400x400.jpg'
image_url = input("enter image url")
image_box = chrome.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]')
image_box.click()
input_box = chrome.find_element_by_tag_name('input')
file_path = '/lhsJS84G_400x400.jpg'

input_box.send_keys(file_path)
#
# import time
#
# time.sleep(2)  # wait for 2 secs
#
# but = chrome.find_element_by_xpath(
#     '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span')
#
# # click the send button
# but.click()
#
# # !wget 'https://pbs.twimg.com/profile_images/1091974962804514817/lhsJS84G_400x400.jpg'
# image_url = input("enter image url")
#
# from getpass import getpass
#
# chrome.get("https://instagram.com")
#
# username = chrome.find_element_by_xpath(
#     '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
# username.send_keys("acanubhav@gmail.com")
#
# password = chrome.find_element_by_xpath(
#     '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
# pswd = getpass()
# password.send_keys(pswd)
# login_btn = chrome.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]')
# login_btn.click()
#
# search_bar = chrome.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
# search_bar.send_keys("shreyasingh4u_")
# time.sleep(3)
# search_bar.send_keys(Keys.ENTER)
# search_bar.send_keys(Keys.ENTER)
#
# post = chrome.find_element_by_xpath(
#     '//*[@id="react-root"]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a/div/div[2]')
# post.click()
# like_btn = chrome.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
# like_btn.click()
# next_btn = chrome.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')
# next_btn.click()
#
# while True:
#     try:
#         like_btn = chrome.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
#         like_btn.click()
#         next_btn = chrome.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
#         next_btn.click()
#         time.sleep(2)
#     except:
#         close_btn = chrome.find_element_by_xpath('/html/body/div[4]/div[3]/button')
#         close_btn.click()
#         break
