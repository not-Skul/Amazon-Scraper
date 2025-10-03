from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium_stealth import stealth

product = input("Which product do you want to search for: ")
last_page = int(input("how many pages do you want to scrape: "))
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=options)
stealth(driver,
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.105 Safari/537.36',
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
options.add_argument("--headless")

books = {
    "book":[],
    "price":[],
    "url":[]
}
for page in range(0,last_page):
    try:
        file = 0
        driver.get(f"https://www.amazon.in/s?k={product}&page={page}&xpid=yZopqwRlcJpnj&crid=236Z2T06V12NZ&qid=1737492515&sprefix=%2Caps%2C556&ref=sr_pg_2")
        # search_box = driver.find_element(by=By.ID,value="twotabsearchtextbox")
        # search_box.send_keys(product)
        # search_box.send_keys(Keys.RETURN)

        items = driver.find_elements(by=By.CLASS_NAME,value="puis-card-container")
        driver.implicitly_wait(10)
        print(f"{len(items)} items discovered")
        for item in items:
            product_name = item.find_element(by=By.CSS_SELECTOR,value="h2").text
            price = item.find_element(by=By.CLASS_NAME,value="a-price-whole").text
            link = item.find_element(by=By.CLASS_NAME, value="a-link-normal").get_attribute("href")
            books["book"].append(product_name)
            books["price"].append(price)
            books["url"].append(link)
        page+=1
    except:
        print("no data available for this product")

list_of_products = pd.DataFrame(books)
print(list_of_products)
# with open("product1.csv","w") as f:
#     f.write(list_of_products)



time.sleep(5)
driver.close()