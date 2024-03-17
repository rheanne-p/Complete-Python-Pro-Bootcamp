from pandas import *
from datetime import datetime
from random import randint
import smtplib

birthdays_csv = read_csv("./birthdays.csv")
birthdays_dict = birthdays_csv.to_dict(orient="index")

today = str(datetime.now())
today_month = int(today.split("-")[1])
today_day = int(today.split("-")[2].split(" ")[0])

for index in birthdays_dict:
    current_entry = birthdays_dict[index]
    current_entry_month = current_entry["month"]
    current_entry_day = current_entry["day"]
    if current_entry_month == today_month and current_entry_day == today_day:
        birthday_entry = current_entry

birthday_name = birthday_entry["name"]
birthday_email = birthday_entry["email"]

random_number = randint(1, 3)
letter_template_file = f"./letter_templates/letter_{random_number}.txt"

with open(file=letter_template_file) as letter_template:
    customized_letter = letter_template.read().replace("[NAME]", birthday_name)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user="appbreweryday32@gmail.com", password="zfzxmqlknzqjkfbf")
    connection.sendmail(
        from_addr="appbreweryday32@gmail.com",
        to_addrs=birthday_email,
        msg=f"Subject:Happy Birthday\n\n{customized_letter}"
    )

print("Email successfully sent!")


