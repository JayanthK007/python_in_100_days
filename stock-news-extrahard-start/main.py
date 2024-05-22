import requests
import os
from twilio.rest import Client
import dotenv


dotenv.load_dotenv()


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
to_phone_number = os.getenv('my_num')

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&outputsize=compact&apikey={os.getenv('API_KEY')}'
r = requests.get(url)
data = r.json()

diff=float(data['Time Series (Daily)']['2024-05-21']['4. close'])-float(data['Time Series (Daily)']['2024-05-20']['4. close'])

percent=diff/float(data['Time Series (Daily)']['2024-05-20']['4. close'])*100

if 5<percent:
    news_data=requests.get(f'https://newsapi.org/v2/everything?q={STOCK}&from=2024-05-20&sortBy=popularity&apiKey={os.getenv('API_KEY_NEWS')}')
    news_data=news_data.json()
    news=[]
    for index in range(0,3):
        news.append({'title':news_data['articles'][index]['title'],'description':news_data['articles'][index]['description']})
       

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+17819902304',
        to=to_phone_number,
        body=f"""{STOCK}: 🔺{int(percent)}
        Headline:{news[0]['title']}
        Brief:{news[0]['description']}
        """
        )

    print(message.status)   
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

