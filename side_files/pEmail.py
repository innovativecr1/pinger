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

# import os

# email = os.getenv("EMAIL")

# if email:
#     print(f"The email is: {email}")
# else:
#     print("Environment variable 'EMAIL' is not set.")

import os

email = os.getenv("EMAIL")
password= os.getenv("PASS")

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_ADDRESS = email
EMAIL_PASSWORD = password

TO_EMAIL = "innovativecreations195@gmail.com"

msg = MIMEMultipart()
msg["From"] = EMAIL_ADDRESS
msg["To"] = TO_EMAIL
msg["Subject"] = "Test Email from Python"

body = "Hello, this is a test email sent from Python!"
msg.attach(MIMEText(body, "plain"))

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    
    server.sendmail(EMAIL_ADDRESS, TO_EMAIL, msg.as_string())
    
    print("Email sent successfully!")
    
    server.quit()

except Exception as e:
    print(f"Error sending email: {e}")
