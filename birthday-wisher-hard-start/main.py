##################### Hard Starting Project ######################
import pandas
import datetime
import random
import smtplib

my_email = "mohana@whatevermail.com"
my_password = "p23isa00!"
data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient='records')
# 1. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
now = datetime.datetime.now()
month = now.month
day = now.day

#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
for r in range(0, len(data_dict)):
    if data_dict[r]['month'] == month and data_dict[r]['day'] == day:
        print(f"{data_dict[r]['month']},{data_dict[r]['day']}")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp
        text_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
        letter = random.choice(text_list)
        with open(f"letter_templates/{letter}", mode='r') as file:
            content = file.read()
            content = content.replace("[NAME]", "Mom")
            print(content)
# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=data_dict[r]['email'],
                    msg=f"Subject: Happy Birthday \n\n "
                        f"{content}")


