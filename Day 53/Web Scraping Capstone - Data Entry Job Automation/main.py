from dataEntryBot import DataEntryBot
from scrapper import Scrapper

bot = DataEntryBot()
scrape = Scrapper()

addresses = scrape.get_addresses()
prices = scrape.get_prices()
links = scrape.get_links()

for num in range(len(addresses)):
    address = addresses[num]
    price = prices[num]
    link = links[num]
    bot.send_data(address, price, link)

bot.create_google_sheet()
