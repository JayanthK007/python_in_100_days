##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
import pandas
import datetime as dt
import random
import smtplib

data =pandas.read_csv("birthdays.csv")
today_day= data["day"].iloc[0]
today_month=data.month.iloc[0]


dob=dt.datetime.now()
current_day=dob.day
current_month=dob.month

if current_day==today_day and current_month==today_month:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    letter_num=random.randint(1,3)
    with open(f'letter_templates/letter_{letter_num}.txt') as file:
            letter=file.readlines()
            name=letter[0][0:5]+"Jayanth,\n"
            letter[0]=name
    # 4. Send the letter generated in step 3 to that person's email address.
    msg="Subject:Happy Birthday\n\n"
    for line in letter:
            msg+=line


    with smtplib.SMTP('smtp.gmail.com',587) as connection:
            connection.starttls()
            connection.login(user='jayanthfaraday@gmail.com',password='add_password')
            connection.sendmail(from_addr='jayanthfaraday@gmail.com',to_addrs='imjayanthkumark@gmail.com',
                                msg=msg)
            



