import time
import json
from selenium import webdriver
from selenium.webdriver.edge.options import Options


def get_items(search, page):
    search = search.replace(" ", "_")
    url = "https://www.alibaba.com/products/{}.html?IndexArea=product_en&page={}".format(
        search, page)
    driver.get(url)

    # sleep for two second then scroll to the bottom of the page
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)  # sleep between loadings

    items = driver.find_elements_by_css_selector(".J-offer-wrapper")
    output = []

    for i in items:

        try:
            name = i.find_element_by_css_selector("h2").text
        except:
            name = None

        try:
            price = i.find_element_by_css_selector(".elements-offer-price-normal__price").text
        except:
            price = None

        try:
            product_url = i.find_element_by_css_selector("h2 a").get_attribute("href")
        except:
            product_url = None

        output_item = {"name": name, "price": price, "url": product_url}
        output.append(output_item)

    return output


# elements-offer-price-normal__price
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Edge(options=chrome_options)

page = 1
search = "glass"
all_items = []
# we will call the function get_items
while True:
    print("getting page", page)
    results = get_items(search, page)
    all_items += results

    if page == 5:
        break

    if len(results) == 0:
        break

    page += 1

# save all the items to a json file
json.dump(all_items, open("product.json", "w"), indent=2)

