import smtplib

my_email = "appbreweryday32@gmail.com"
app_password = "zfzxmqlknzqjkfbf"

# Object of SMTP class
# connects to email providers' SMTP servers
connection = smtplib.SMTP("smtp.gmail.com")
#                     location of gmail's server

# Transport Layer Security
# secures connection to email server (encrypted)
connection.starttls()

# Log into Email Provider (sender)
connection.login(user=my_email, password=app_password)

# Send Email
connection.sendmail(
    from_addr=my_email,
    to_addrs="pythonrecipientday32@yahoo.com",
    msg="Subject:Hello\n\nThis is the body of my email"
    #        two new lines for content
)
connection.close()


# with... as... keywords
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=app_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="pythonrecipientday32@yahoo.com",
        msg="Subject:Hello\n\nThis is the body of my email"
    )
