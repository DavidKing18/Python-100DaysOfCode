import requests
from bs4 import BeautifulSoup
import lxml
from smtplib import SMTP
import os

my_email = "cornflakeschicago@gmail.com"
password = os.environ["CHICAGO_MAIL_PASSWORD"]
receiver_email = "davidoadeleke90@gmail.com"

URL = "https://www.amazon.com/Apple-MacBook-Laptop-12%E2%80%91core-19%E2%80%91core/dp/B0BSHDJG9T/ref=sr_1_1?crid" \
      "=1089R52W08LJW&keywords=macbook+pro&qid=1676691862&sprefix=mac%2Caps%2C330&sr=8-1"

header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 "
                  "Safari/537.36 Edg/109.0.1518.70"
}

response = requests.get(url=URL, headers=header)
amazon_website = response.text

soup = BeautifulSoup(amazon_website, "lxml")
price_with_currency = soup.select_one(selector="tr td .a-text-price span").string
price_without_currency = float("".join(price_with_currency[1:].split(",")))

PRESET_PRICE = 2000

if price_without_currency <= PRESET_PRICE:
    message = "Apple 2023 MacBook Pro Laptop M2 Pro chip with 12‑core CPU and 19‑core GPU: 16.2-inch Liquid Retina " \
              "XDR Display, 16GB Unified Memory, 512GB SSD Storage. Works with iPhone/iPad; Space Gray"
    with SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=receiver_email, msg=f"Subject: Amazon Price Alert!! "
                                                                             f"\n\n{message}, is now "
                                                                             f"{price_with_currency}.\n"
                                                                             f"{URL}".encode("utf-8"))
