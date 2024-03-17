import smtplib
import datetime as dt
import random

my_email = "appbreweryday32@gmail.com"
app_password = "zfzxmqlknzqjkfbf"

now = dt.datetime.now()
current_day_of_week = now.weekday()


if current_day_of_week == 5:
    with open("quotes.txt", mode="r") as quotes:
        quotes_list = quotes.readlines()
        random_quote = random.choice(quotes_list)
        print(random_quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="pythonrecipientday32@yahoo.com",
            msg=f"Subject:Saturday Motivation\n\n{random_quote}"
        )
