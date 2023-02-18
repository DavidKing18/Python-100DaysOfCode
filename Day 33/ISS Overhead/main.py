import time
import requests
from datetime import datetime
import smtplib
import os

MY_LAT = 6.524379  # Your latitude
MY_LONG = 3.379206  # Your longitude
MY_EMAIL = "cornflakeschicago@gmail.com"
PASSWORD= os.environ["CHICAGO_MAIL_PASSWORD"]
RECEIVER_ADDRESS = "davidoadeleke90@gmail.com"


# Your position is within +5 or -5 degrees of the ISS position.
def is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True
    else:
        return False


# If the ISS is close to my current position,
# and it is currently dark
# Then email me to tell me to look up.
# BONUS: run the code every 60 seconds.


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    current_hour = time_now.hour

    if current_hour >= sunset:
        return True
    else:
        return False


while True:
    if is_close() and is_dark():
        with smtplib.SMTP("smtp.gmail.com", 547) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECEIVER_ADDRESS,
                                msg="Subject: Look Up! \n\nCheck the sky "
                                    "now, ""ISS is passing")
    time.sleep(60)
