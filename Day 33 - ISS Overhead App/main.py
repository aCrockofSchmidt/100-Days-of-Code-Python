import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.048615 # Your latitude
MY_LONG = -114.070847 # Your longitude


def iss_check():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.utcnow()

    is_close = False
    is_dark = False

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        is_close = True
    else:
        print("Not in range.")

    if sunset <= time_now.hour <= sunrise:
        is_dark = True
    else:
        print("Not dark yet.")

    if is_close and is_dark:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user="the.legendary.flush@gmail.com", password="vccbbkrijzbuovus")
            connection.sendmail(
                from_addr="the.legendary.flush@gmail.com",
                to_addrs="the_legendary_flush@yahoo.com",
                msg="Subject: \n\n The ISS is in view.  LOOK UP!"
            )
            return
    time.sleep(60)
    iss_check()


iss_check()



#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.






