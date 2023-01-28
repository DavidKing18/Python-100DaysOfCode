import datetime as dt
import smtplib
from random import choice

current_date = dt.datetime.now()
current_weekday = current_date.weekday()

with open("quotes.txt") as quote_file:
    list_of_quotes = quote_file.readlines()
    message = choice(list_of_quotes)

if current_weekday == 5 or current_date == 1:
    my_email = "cornflakeschicago@gmail.com"
    password = "tsjkmtsobmqbolxg"
    receiver_address = "davidoadeleke90@gmail.com"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=receiver_address, msg=f"Subject: Monday Motivation\n\n"
                                                                               f"{message}")
