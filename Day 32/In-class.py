############################################################
#       How to Send Emails with Python using SMTP
############################################################
#
import smtplib

my_email = "cornflakeschicago@gmail.com"
password = "tsjkmtsobmqbolxg"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()

    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="davidoadeleke90@gmail.com", msg="Hello")

#
# my_email = "chickennoodlesjazz@yahoo.com"
# password = "nasconasco1$"
#
# with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="cornflakeschicago@gmail.com", msg="Hello")


############################################################
#       Working with the datetime Module
############################################################

import datetime as dt

now = dt.datetime.now()
current_year = now.year
print(now)
print(current_year)

if current_year == 2023:
    day_of_week = now.weekday()
    print(day_of_week, "\n")

date_of_birth = dt.datetime(year=2002, month=10, day=18)
print(date_of_birth)
