import datetime as dt
import smtplib
from random import randint
import pandas

now = dt.datetime.now()
current_month = now.month
current_day = now.day

people = pandas.read_csv("birthdays.csv")
people_list = people.to_dict(orient="records")

for person in people_list:
    if person["month"] == current_month and person["day"] == current_day:
        num = randint(1, 3)
        name_of_celebrant = person["name"]
        celebrant_email = person["email"]
        my_email = "cornflakeschicago@gmail.com"
        password = "tsjkmtsobmqbolxg"
        with open(f"letter_templates/letter_{num}.txt") as birthday_letter:
            message = birthday_letter.read().replace("[NAME]", name_of_celebrant)
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=celebrant_email,
                                    msg=f"Subject: Happy Birthday {name_of_celebrant}!\n\n{message}")

##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
