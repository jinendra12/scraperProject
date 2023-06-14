from bs4 import BeautifulSoup
import requests


def get_coinmarketcap_data():
    response = requests.get("https://coinmarketcap.com/")
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table", class_="cmc-table")
    rows = table.find_all("tr", limit=None)

    data = []
    for row in rows:
        cols = row.find_all("td")

        data.append({
            "name": cols[2].text if len(cols) > 2 else "",
            "price": cols[3].text if len(cols) > 3 else "",
            "percent_1h": cols[4].text if len(cols) > 4 else "",
            "percent_24h": cols[5].text if len(cols) > 5 else "",
            "percent_7d": cols[6].text if len(cols) > 6 else "",
            "market_cap": cols[7].text if len(cols) > 7 else "",
            "volume_24h": cols[8].text if len(cols) > 8 else "",
            "circulating_supply": cols[9].text if len(cols) > 9 else ""
        })
    return data


def update_values():
    post_url = "http://127.0.0.1:8000/update_coin_market_data/"

    data = get_coinmarketcap_data()
    print("suc got data from scrapper")
    headers = {
        'Content-Type': 'application/json'
    }
    requests.post(post_url, json=data, headers=headers)
