from bs4 import BeautifulSoup
import requests

URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C" \
      "%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122" \
      ".30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22" \
      "%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D" \
      "%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22" \
      "%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B" \
      "%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price" \
      "%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom" \
      "%22%3A12%7D"

header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 "
                  "Safari/537.36 Edg/109.0.1518.70"
}


class Scrapper:

    def __init__(self):
        self.response = requests.get(URL, headers=header)
        self.zillow_website = self.response.text
        self.soup = BeautifulSoup(self.zillow_website, "html.parser")

    def get_addresses(self):
        addresses = [address.string for address in self.soup.select(selector=".property-card-data a address")]
        return addresses

    def get_prices(self):
        prices = [price.string[:6] for price in self.soup.select(selector=".gMDnGj span")]
        return prices

    def get_links(self):
        links = [link.get("href") for link in self.soup.select(selector=".property-card-data a")]
        formatted_links = []
        for link in links:
            if "https://www.zillow.com" not in link:
                link = "https://www.zillow.com" + link
            formatted_links.append(link)
        return formatted_links
