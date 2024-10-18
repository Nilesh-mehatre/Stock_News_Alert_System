# Stock News Alert System

## Overview
The **Stock News Alert System** is a Python-based application that fetches the latest stock price data for a specified company and sends SMS alerts with news updates when significant price changes occur. By integrating the Alpha Vantage API for stock data and the News API for relevant news articles, this project provides real-time insights directly to your mobile device using Twilio.

## Features
- Fetches daily stock prices for a specified company.
- Calculates the percentage change in stock price from the previous day.
- Sends SMS alerts with news headlines when the stock price changes significantly.
- Customizable company symbol and recipient phone number.

## APIs Used
- **Alpha Vantage**: Provides stock price data. [API Documentation](https://www.alphavantage.co/documentation/)
- **News API**: Fetches the latest news articles related to the specified company. [API Documentation](https://newsapi.org/docs/getting-started)
- **Twilio**: Sends SMS notifications with the latest stock updates and news. [API Documentation](https://www.twilio.com/docs/sms)

## Requirements
- Python 3.x
- `requests` library
- `twilio` library

## Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Stock_News_Alert_System.git
   cd stock-news-alert-system
