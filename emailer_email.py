"""
***********************************************************************************
    Attaches the document generated from the Template and and sends a customised
                            email to the users email address
***********************************************************************************
"""
import smtplib
from decouple import config


# Retrieving our configuration requirement
EMAIL_ADDRESS = config("EMAIL_ADDRESS")
EMAIL_PASS = config("EMAIL_PASS")

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    # encrypting our mail server
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    # login in to our gmail using environment variables
    smtp.login(EMAIL_ADDRESS, EMAIL_PASS)

    # creating a simple meassage
    subject = "Hello User"
    body = "How are you doing"

    msg = f"Subject: {subject}\n\n{body}"

    # sending the email
    smtp.sendmail(EMAIL_ADDRESS, "sample-email@gmail.com", msg)



