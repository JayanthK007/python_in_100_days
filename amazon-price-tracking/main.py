from bs4 import BeautifulSoup
import requests
import smtplib
import os, dotenv

dotenv.load_dotenv()


response=requests.get('https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6',headers={
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    "Accept-Language":'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7,kn;q=0.6'
})


soup=BeautifulSoup(response.text,'html.parser')
whole_part=(soup.find('span',attrs={'class':"a-price-whole"}).contents[0])
fraction_part=(soup.find('span',attrs={'class':"a-price-fraction"}).contents[0])
price=float(whole_part+'.'+fraction_part)


if(price<100):
    with smtplib.SMTP(host='smtp.gmail.com',port=587) as connection:
        connection.starttls()
        connection.login(user=os.getenv('SMPT_SENDER'),password=os.getenv('SMTP_PASSWORD'))
        connection.sendmail(from_addr=os.getenv('SMPT_SENDER'),to_addrs=os.getenv('SMTP_RECEIVER'),
                msg=f"Subject:Amazon Price Alert! \n\n Instant Pot Duo Plus 9-in-1 Electric Pressure Cooker, Slow Cooker, Rice Cooker, Steamer, Sauté, Yogurt Maker, Warmer & Sterilizer, Includes App With Over 800 Recipes, Stainless Steel, 3 Quart is now ${price}".encode('utf-8'))
        connection.close()
