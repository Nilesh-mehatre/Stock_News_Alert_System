import requests
from twilio.rest import Client

# Replace these with your actual API keys and tokens or set them in your environment variables
API_KEY = ''  # Alpha Vantage API key
NEWS_API = ''  # News API key
TWILIO_AUTH_TOKEN = ''  # Twilio Auth Token
ACCOUNT_SID_TWILIO = ''  # Twilio Account SID
TWILIO_NUMBER = ''  # Your Twilio phone number
COMPANY = 'IBM'  # Company symbol for stock

# Set up parameters for the stock API request
stock_param = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': COMPANY,
    'apikey': API_KEY,
    'outputsize': 'compact'
}

# Endpoints for stock and news APIs
STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
NEWS_ENDPOINT = 'https://newsapi.org/v2/top-headlines'

# Get stock data
r = requests.get(STOCK_ENDPOINT, params=stock_param)
data = r.json()

# Extract stock data
stock_data = data["Time Series (Daily)"]
stock_dates = list(stock_data.keys())

# Get closing prices
yesterday_closing_price = float(stock_data[stock_dates[0]]["4. close"])
day_before_yesterday_closing_price = float(stock_data[stock_dates[1]]["4. close"])

# Determine price change direction and percentage
price_change = yesterday_closing_price - day_before_yesterday_closing_price
symbol = '+' if price_change > 0 else '-'
percentage_change = abs((price_change / day_before_yesterday_closing_price) * 100)

# Send news updates if the stock price changed significantly
if percentage_change > 1:
    news_api_param = {
        'q': COMPANY,
        'apiKey': NEWS_API
    }
    response = requests.get(NEWS_ENDPOINT, params=news_api_param)
    news_data = response.json()
    news_articles = news_data['articles'][:3]  # Get top 3 articles

    formatted_articles = [
        f'STOCK UPDATE: {COMPANY} {percentage_change:.2f}% {symbol}\n'
        f'Source: {article["source"]["name"]}\n'
        f'Headline: {article["title"]}\n'
        f'Brief: {article["description"]}'
        for article in news_articles
    ]

    # Create a Twilio client
    client = Client(ACCOUNT_SID_TWILIO, TWILIO_AUTH_TOKEN)

    # Send each news article as a message
    for news in formatted_articles:
        to_number = 'recipient_phone_number'  # Replace with the recipient's phone number
        message = client.messages.create(
            body=news,
            from_=TWILIO_NUMBER,
            to=to_number
        )
