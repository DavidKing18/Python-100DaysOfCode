import requests
from twilio.rest import Client
import math
import os
import html

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

MY_STOCK_API_KEY = "FYZTTR3OY2V60UXN"
MY_NEWS_API_KEY = "6e9a444499cf4cf7be50fb2ceb722911"

account_sid = "ACca0ea5bd6df26df15bd88fb8c9a86e0f"
auth_token = os.environ["AUTH_TOKEN"]

parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "interval": "5min",
    "apikey": MY_STOCK_API_KEY
}

response = requests.get("https://www.alphavantage.co/query?", params=parameters)
data = response.json()

all_data = [value for value in data["Time Series (Daily)"].values()]
yesterday_data = all_data[0]
previous_day_data = all_data[1]

yesterday_close = float(yesterday_data['4. close'])
previous_close = float(previous_day_data['4. close'])

if yesterday_close > previous_close:
    direction = "🔺"
    percent_price_change = math.ceil((yesterday_close - previous_close) * 100/yesterday_close)
else:
    direction = "🔻"
    percent_price_change = math.floor(-((yesterday_close - previous_close) * 100/yesterday_close))

if percent_price_change >= 3:
    news_parameters = {
        "q": COMPANY_NAME,
        "apikey": MY_NEWS_API_KEY
    }
    news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
    news_data = news_response.json()
    articles = news_data["articles"]
    first_3_articles = articles[:3]
    for article in first_3_articles:
        headline = html.unescape(article['title'])
        description = html.unescape(article['description'])
        alert = f"{STOCK}: {direction}{percent_price_change}%\nHeadline: {headline}\nBrief: {description}"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=alert,
            from_="+12058329459",
            to='+2348083603251'
        )
        print(alert, "\n")
        print(message.status)



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
