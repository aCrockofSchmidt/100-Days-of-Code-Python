##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import random
import pandas as pd
import os

# access birthday information in csv file

with open("birthdays.csv") as data:
    birthdays = pd.read_csv(data)

# access current date information

now = dt.datetime.now()
current_month = now.month
current_day = now.day

# determine if date match exists

matches = birthdays[(birthdays.month == current_month) & (birthdays.day == current_day)]

if len(matches) != 0:
    path = os.path.join("letter_templates/", random.choice(os.listdir("letter_templates")))

    with open(path, "r") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", matches.name.item())

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user="the.legendary.flush@gmail.com", password="vccbbkrijzbuovus")
        connection.sendmail(
            from_addr="the.legendary.flush@gmail.com",
            to_addrs=matches.email.item(),
            msg=f"Subject: HAPPY BIRTHDAY!\n\n{letter}"
        )
else:
    print("Sorry.  No birthdays today.")
