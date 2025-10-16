TSLA Stock Alert

This Python script monitors Tesla’s stock price and sends an email alert with the top news article if the price changes by 5% or more.

Features

Fetches the latest two trading days from Alpha Vantage.

Calculates if Tesla stock has increased or decreased by 5% or more.

Retrieves the top news article about Tesla from NewsAPI.

Sends a simple email alert with the news and emoji indicating stock movement.

Setup

* Get your Alpha Vantage API key: https://www.alphavantage.co

* Get your NewsAPI key: https://newsapi.org

* Create a Gmail App Password for sending emails: Google App Passwords

Update the script:

* If Tesla stock moves ≥5%, an email is sent with the latest news article.

* Email includes a 🔺 or 🔻 emoji to indicate increase or decrease.

Notes

* Works best on trading days; weekends/holidays are automatically handled.

* Free API keys have request limits:

* Alpha Vantage: 25 requests/day

* NewsAPI: 100 requests/day

* The script is functional but not perfect. 
