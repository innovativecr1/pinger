# import smtplib
# # creates SMTP session
# s = smtplib.SMTP('smtp.gmail.com', 587)
# # start TLS for security
# s.starttls()
# # Authentication
# s.login("", "")
# # message to be sent
# message = "Message_you_need_to_send"
# # sending the mail
# s.sendmail("dummyemailsmtplib@gmail.com", "innovativecreations195gmail.com", message)

# s.quit()

import os

email = os.getenv("EMAIL")

if email:
    print(f"The email is: {email}")
else:
    print("Environment variable 'EMAIL' is not set.")