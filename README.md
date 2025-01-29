# Pinger

It will notify you if any channel upload a new video through email.
The data.json file contains the channel deatils.
You have to change data.json file according to your need.

## Steps to setup the project

Python 3.13.1

#Some steps which are not required but are recommended:
-- Create a virtual environment
-- Activate it

1. Run the requirement file 
pip install -r requirements.txt

2. Enable 2 step authentication then create app password from your google account(recommended) or you can try using the normal email id and password

3. create environment variables: 
    1. "EMAIL": 
        $env:EMAIL = "senderemail@mail.com"
    2. "PASS":
        $env:PASS = "emailpassword"

4. Change TO_EMAIL = "emailtobepinged@gmail.com", to which you want to be pinged.

5. Download the chromedriver according to the version of your chrome browser and paste it inside the project("/") folder.

6. Run the file.

