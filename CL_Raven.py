#! /usr/bin/env python3

import smtplib
import getpass

# Here lies your victim stash.
receivers = ['email_one@domain.com', 'email_two@domain.com']
# They stole your private information - you stole their inbox space.

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
# Created SMTP object, passed domain and port as args. This represents our connection to an SMTP server
## And holds methods for sending emails.

type(smtpObj) # Say hello to the SMTP email server.
# We need this object, so if this call is unsuccessful, our SMTP server might not support TLS on port 587
## If that's the case, we need to create an SMTP object with SSL on port 465.
# -> smtplib.SMTP_SSL('smtp.emailhandle.com', 465)
smtpObj.ehlo()
# If the tuple returned begins with 250, we're successful in our greeting.

smtpObj.starttls() #If using port 465 - This TLS method can be skipped.
# If the tuple returned begins with 220 - the server is ready.

username = input('Username: ')
password = getpass.getpass('Password: ')

smtpObj.login(username, password)
# Method call logging in for you, using your credentials.


smtpObj.sendmail('your_email_@domain.com', receivers,
'Subject: Here is your subject line.\
Here is the body of your email message. \nCheers.')

print("Your email as been sent.")

# We should receive an empty dictionary, if this is successful.
smtpObj.quit()
# Disconnects from the SMTP Server.