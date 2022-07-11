# deals with attaching the document to the email and sending of
# emails to their various SMTP
import smtplib
from decouple import config


# Retrieving our configuration requirement
EMAIL_ADDRESS = config("EMAIL_ADDRESS")
EMAIL_PASS = config("EMAIL_PASS")

