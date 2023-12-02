import smtplib
import datetime as dt
import random

# my_email = "test@gmail.com"
# my_password = "@123456<>M"
# their_email = "not_test@yahoo.com"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     # This line makes the connection secure. If someone were to intercept the email, it would be encrypted.
#
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email, to_addrs=their_email, msg="Subject: Hey there \n\n Hello")
#     # The \n\n is required to differentiate between the subject line and body of the email


# now = dt.datetime.now()
# year = now.year
# month = now.month
# print(f"{year}, {month}")
#
# date_of_birth = dt.datetime(year=1997, month=9, day=1, hour=6)
# print(date_of_birth)


# ----------------------- #MondayMotivation Email --------------------- #
with open("quotes.txt") as quotes:
    quote_data = quotes.readlines()
    random_quote = random.choice(quote_data)
    now = dt.datetime.now()
    day = now.weekday()
    print(day)

    if day == 4:
        my_email = "test@gmail.com"
        my_password = "@123456<>M"
        their_email = "not_test@yahoo.com"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=their_email,
                msg=f"Subject: #MondayMotivation \n\n "
                    f"{random_quote}")


