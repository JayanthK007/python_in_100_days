# import smtplib

# my_email="jayanthfaraday@gmail.com"
# password='add_password'
# with smtplib.SMTP('smtp.gmail.com',587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs='imjayanthkumark@gmail.com',
#                         msg="Subject:Hello\n\n Jayanth This is the body of the email.")

# import datetime as dt

# now=dt.datetime.now()
# year=now.year
# month=now.month
# week_day=now.weekday()
# print(year)
# print(month)
# print(week_day)

# date_of_birth=dt.datetime(year=1999,month=11,day=13)


import datetime as dt
import smtplib
import random

current_day=dt.datetime.now()

current_day=current_day.weekday()
print(current_day)

if current_day==6:
    with open('quotes.txt') as file:
        quotes=file.readlines()

    quote=random.choice(quotes)    
    my_email="jayanthfaraday@gmail.com"
    password='add_password'
    with smtplib.SMTP('smtp.gmail.com',587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs='imjayanthkumark@gmail.com',
                            msg="Subject:Sunday quote\n\n"+quote)
