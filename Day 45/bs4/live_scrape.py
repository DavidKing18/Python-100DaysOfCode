#########################################
#        Scraping a Live Website
#########################################

import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.select(selector=".titleline a")

article_texts = []
article_links = []

filters = soup.select(selector=".sitebit a")
for element in filters:
    articles.remove(element)

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag['href']  # OR article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.select(selector=".subline .score")]

print(article_texts)
print(article_links)
print(article_upvotes)

larger_number = max(article_upvotes)
highest_upvote_index = article_upvotes.index(larger_number)
highest_upvote_title = article_texts[highest_upvote_index]
highest_upvote_link = article_links[highest_upvote_index]
print()

print(highest_upvote_index)
print(f"Hot News: {highest_upvote_index+1}. {highest_upvote_title}")
print("Link: ", highest_upvote_link)
