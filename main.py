import requests
import smtplib

# Check Stocks

EMAIL = "jomirbautista.comcave@gmail.com"
EMAIL_APP_PASSWORD = "ENTER APP PASSWORD HERE"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_API_KEY = "ENTER ALPHAVANTAGE API KEY"
ENDPOINT = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={ALPHAVANTAGE_API_KEY}"

response = requests.get(ENDPOINT)
response.raise_for_status()
data = response.json()

time_series = data["Time Series (Daily)"]
dates = sorted(time_series.keys(), reverse=True)
latest_date = dates[0]
previous_date = dates[1]

open1 = float(time_series[latest_date]["1. open"])
open2 = float(time_series[previous_date]["1. open"])

five_percent = open1 * 0.05

# News API

NEWS_API = "ENTER NEWS API"
NEWS_ENDPOINT = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from={latest_date}&sortBy=popularity&apiKey={NEWS_API}"

news_response = requests.get(NEWS_ENDPOINT)
news_response.raise_for_status()
news_data = news_response.json()

article1_title = news_data["articles"][0]["title"]
article1_url = news_data["articles"][0]["url"]

article2_title = news_data["articles"][1]["title"]
article2_url = news_data["articles"][1]["url"]

article3_title = news_data["articles"][2]["title"]
article3_url = news_data["articles"][2]["url"]

# Send email

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=EMAIL, password=EMAIL_APP_PASSWORD)

if open1 >= open2 + five_percent:
    message = (f"TSLA 🔺 \n\n{article1_title} \n {article1_url}"
               f"\n\n{article2_title} \n {article2_url}"
               f"\n\n{article3_title} \n {article3_url}")
    connection.sendmail(from_addr=EMAIL,
                        to_addrs="jomir.bautista@gmail.com",
                        msg=message)
elif open1 <= open2 - five_percent:
    message = (f"TSLA 🔻 \n\n{article1_title} \n {article1_url}"
               f"\n\n{article2_title} \n {article2_url}"
               f"\n\n{article3_title} \n {article3_url}")
    connection.sendmail(from_addr=EMAIL,
                        to_addrs="jomir.bautista@gmail.com",
                        msg=message)

connection.quit()
