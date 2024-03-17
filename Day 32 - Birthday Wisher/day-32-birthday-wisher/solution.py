import datetime as dt
import pandas
import random
import smtplib

today_tuple = (dt.datetime.now().month, dt.datetime.now().day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    with open(file_path) as letter_file:
        contents = letter_file.read()
        new_letter = contents.replace("[NAME]", birthday_person["name"])
        print(new_letter)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        MY_EMAIL = "appbreweryday32@gmail.com"
        MY_PASS = "zfzxmqlknzqjkfbf"
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Solution\n\n{new_letter}"
        )
