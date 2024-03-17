import datetime as dt
import pandas
import random
import smtplib

today = dt.datetime.now()
month = today.month
day = today.day

birthdays_file = pandas.read_csv("birthdays.csv")
months_list = birthdays_file.month.to_list()
days_list = birthdays_file.day.to_list()

if month in months_list and day in days_list:
    row = birthdays_file[birthdays_file.month == month]
    name = row.name.to_string(index=False)
    email = row.email.to_string(index=False)

    random_letter = str(random.randint(1, 3))
    letter_file_name = "letter_" + random_letter + ".txt"
    print(f"Successfully sent {letter_file_name} to {name}.")

    with open(f"./letter_templates/{letter_file_name}") as letter_file:
        contents = letter_file.read()
        final_letter = contents.replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        SENDER_EMAIL = "appbreweryday32@gmail.com"
        APP_PASS = "zfzxmqlknzqjkfbf"
        RECIPIENT_EMAIL = email
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=APP_PASS)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=RECIPIENT_EMAIL,
            msg="Subject:Happy Birthday!\n\n" + final_letter
        )
else:
    print("It isn't anybody's birthday today.")
