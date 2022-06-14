import datetime as dt
import random
import smtplib
import smtplib

MY_EMAIL = "caseclass123@gmail.com"
MY_PASSWORD = "Demo@1234"
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quote.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )