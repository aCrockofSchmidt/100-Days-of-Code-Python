import requests
import datetime as dt
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc."

alpha_api_key = os.environ.get("ALPHA_API_KEY")
alpha_url = "https://www.alphavantage.co/query"
alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alpha_api_key
}

news_api_key = os.environ.get("NEWS_API_KEY")
news_url = "https://newsapi.org/v2/everything"
news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": news_api_key,
}

account_sid = "AC7bfad92a7d8c6c80bbc36d26aab22574"
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")


def find_days_back(date, data):
    days_back = 1

    while str(date - dt.timedelta(days=days_back)) not in data["Time Series (Daily)"]:
        days_back += 1

    return days_back


# Get Data from Stock Info Provider API

response = requests.get(url=alpha_url, params=alpha_parameters)
response.raise_for_status()
stock_data = response.json()

# Find previous two trading days

today = dt.date.today()
yesterday = today - dt.timedelta(days=find_days_back(today, stock_data))
day_before_yesterday = yesterday - dt.timedelta(days=find_days_back(yesterday, stock_data))

# find closing prices for stock on each day

yesterday_close = stock_data["Time Series (Daily)"][str(yesterday)]["4. close"]
day_before_yesterday_close = stock_data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"]

# determine if alert should be sent

daily_change = -((float(yesterday_close) - float(day_before_yesterday_close))/float(day_before_yesterday_close))

if daily_change <= -0.000005 or daily_change >= 0.000005:

# retrieve news stories from news api

    response = requests.get(url=news_url, params=news_parameters)
    response.raise_for_status()
    news_data = response.json()

    news_articles = news_data["articles"][:3]

# format results for text messaging

    if daily_change >= 0:
        percent_change = "▲ " + '{:.0%}'.format(daily_change)
    else:
        percent_change = "▼ " + '{:.0%}'.format(daily_change)

    sms_message = f"\n\n{COMPANY_NAME}: {percent_change}\n" \
                  f"Headline: {news_articles[0]['title']}\n" \
                  f"Brief: {news_articles[0]['description']}\n\n" \
                  f"{COMPANY_NAME}: {percent_change}\n" \
                  f"Headline: {news_articles[1]['title']}\n" \
                  f"Brief: {news_articles[1]['description']}\n\n" \
                  f"{COMPANY_NAME}: {percent_change}\n" \
                  f"Headline: {news_articles[2]['title']}\n" \
                  f"Brief: {news_articles[2]['description']}"

# send sms message to phone

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=sms_message,
        from_='+18482175388',
        to='+15877774433'
    )
    print(message.status)
