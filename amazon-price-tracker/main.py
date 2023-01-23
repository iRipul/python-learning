from bs4 import BeautifulSoup
import requests

url = "https://www.amazon.com/Instant-Pot-Plus-Programmable-Sterilizer/dp/B075CWJ3T8?th=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(url, headers=headers).text

soup = BeautifulSoup(response, "html.parser")

whole_price = soup.select_one("span.a-price-whole").getText()
fraction_price = soup.select_one("span.a-price-fraction").getText()

price = float(f"{whole_price}{fraction_price}")

target_price = 199.99

if price <= target_price:
    print("The price is less than the target price. please go ahead and purchase the item")
else:
    print("The price is still higher than the target price. please be patient and wait for good days.")
