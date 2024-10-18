# 📈 Stock News Alert System 📬

## Overview
The **Stock News Alert System** is a Python-based application that fetches the latest stock price data for a specified company and sends SMS alerts with news updates when significant price changes occur. By integrating the Alpha Vantage API for stock data and the News API for relevant news articles, this project provides real-time insights directly to your mobile device using Twilio.

## Features
- 📊 Fetches daily stock prices for a specified company.
- 📉 Calculates the percentage change in stock price from the previous day.
- 📲 Sends SMS alerts with news headlines when the stock price changes significantly.
- 🔄 Customizable company symbol and recipient phone number.

## APIs Used
- **Alpha Vantage**: Provides stock price data. [API Documentation](https://www.alphavantage.co/documentation/)
- **News API**: Fetches the latest news articles related to the specified company. [API Documentation](https://newsapi.org/docs/getting-started)
- **Twilio**: Sends SMS notifications with the latest stock updates and news. [API Documentation](https://www.twilio.com/docs/sms)

## Requirements
- 🐍 Python 3.x
- 📦 `requests` library
- 📱 `twilio` library

## Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Stock_News_Alert_System.git
   cd stock-news-alert-system
3. **Obtain API Keys**:
Sign up for Alpha Vantage and get your API key.
Sign up for News API and get your API key.
Sign up for Twilio and obtain your Account SID, Auth Token, and a Twilio phone number.
4. **Configure Environment Variables**:
Set the following environment variables or replace them directly in the code:

API_KEY: Alpha Vantage API key
NEWS_API: News API key
TWILIO_AUTH_TOKEN: Twilio Auth Token
ACCOUNT_SID_TWILIO: Twilio Account SID
TWILIO_NUMBER: Your Twilio phone number
5. **Run the Script**:
Update the COMPANY variable with the desired stock symbol and the recipient's phone number in the script, then run:

bash
Copy code
python main.py
Usage
Once the script is running, it will check the stock price daily and send SMS alerts with news updates if the price change exceeds a specified threshold (currently set to 1%).

Contributing
🤝 Contributions are welcome! Please feel free to submit a pull request or open an issue for suggestions or improvements.

### Added Instructions:
- Clearly listed the steps to **install required libraries** and **obtain API keys**.
- Organized the instructions to enhance clarity, making it easier for users to follow.

Feel free to modify any part further based on your preferences!

