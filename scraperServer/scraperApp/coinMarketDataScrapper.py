from argparse import Action

from bs4 import BeautifulSoup
import requests
import time

from selenium.webdriver.common.by import By


# def get_coinmarketcap_data():
#     response = requests.get("https://coinmarketcap.com/")
#     time.sleep(5)
#     soup = BeautifulSoup(response.content, "html.parser")
#
#     table = soup.find("table", class_="cmc-table")
#     rows = table.find_all("tr", limit=100)
#
#     data = []
#     for row in rows:
#         cols = row.find_all("td")
#
#         data.append({
#             "name": cols[2].text if len(cols) > 2 else "",
#             "price": cols[3].text if len(cols) > 3 else "",
#             "percent_1h": cols[4].text if len(cols) > 4 else "",
#             "percent_24h": cols[5].text if len(cols) > 5 else "",
#             "percent_7d": cols[6].text if len(cols) > 6 else "",
#             "market_cap": cols[7].text if len(cols) > 7 else "",
#             "volume_24h": cols[8].text if len(cols) > 8 else "",
#             "circulating_supply": cols[9].text if len(cols) > 9 else ""
#         })
#     return data

def get_coinmarketcap_data():
    from selenium import webdriver

    driver = webdriver.Chrome()

    url = "https://coinmarketcap.com/"

    driver.get(url)

    scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
    scroll_step = 250

    while scroll_height > 0:
        driver.execute_script(f"window.scrollBy(0, {scroll_step});")
        time.sleep(0.1)
        scroll_height -= scroll_step

    table = driver.find_elements(By.TAG_NAME, "table")
    table = table[0]

    data = table.find_elements(By.TAG_NAME, "tr")

    res = []

    for row in data:
        col = row.find_elements(By.TAG_NAME, "td")
        length = len(col)

        name = col[2].text if length > 2 else ""
        price = col[3].text if length > 3 else ""
        percent_1h = col[4].text if length > 4 else ""
        percent_24h = col[5].text if length > 5 else ""
        percent_7d = col[6].text if length > 6 else ""
        market_cap = col[7].text if length > 7 else ""
        volume_24h = col[8].text if length > 8 else ""
        circulating_supply = col[9].text if length > 9 else ""

        crypto = {
            "name": name,
            "price": price,
            "percent_1h": percent_1h,
            "percent_24h": percent_24h,
            "percent_7d": percent_7d,
            "market_cap": market_cap,
            "volume_24h": volume_24h,
            "circulating_supply": circulating_supply
        }

        res.append(crypto)

    driver.close()
    return res


def update_values():
    post_url = "http://127.0.0.1:8000/update_coin_market_data/"

    data = get_coinmarketcap_data()
    headers = {
        'Content-Type': 'application/json'
    }
    requests.post(post_url, json=data, headers=headers)
