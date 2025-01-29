TO_EMAIL = "emailtobepinged@gmail.com"

import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def sendMail( recieversEmail, sub, body,):
    EMAIL_ADDRESS = os.getenv("EMAIL")
    EMAIL_PASSWORD= os.getenv("PASS")
 
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = recieversEmail
    msg["Subject"] = sub

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


def get_video_count(channel_url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver_service = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=driver_service, options=chrome_options)
    driver.get(channel_url)

    try:
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-tabbed-page-header/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/div/div[2]/yt-page-header-renderer/yt-page-header-view-model/div/div[1]/div/yt-content-metadata-view-model/div[2]/span[3]/span")
        ))
        video_count = int(element.text.split(" ")[0])
        return video_count
    except Exception as e:
        raise Exception(f"Failed to fetch video count: {e}")
    finally:
        driver.quit()


def newVideo(videos, channel):
    print(f"New video uploaded😍, {channel}")
    newData = { 'videos': videos}


def sameVideos(channel):
    print(f"Nothing new😢, {channel}")



if __name__ == "__main__":

    data = open("data.json")
    dataJson = json.load(data)

    newData = []
    for d in dataJson:
        print(d)
        channelName = d["channel"]
        newDict = d
        channel_url = f"https://www.youtube.com/@{channelName}"
        try:
            video_count = get_video_count(channel_url)
            print(f"The channel has {video_count} videos.")
            initialVideoCount = d["videos"]

            if initialVideoCount < video_count:
                newDict["videos"] = video_count
                newData.append(newDict)
            
                newVideo(video_count, channelName)
                sub = "Pinger, New video found"
                msg = f"""New video has been uploaded to {channelName} 😍
                {channel_url}"""
                sendMail(TO_EMAIL, sub, msg)
            else:
                sameVideos(channelName)
        except Exception as e:
            print(f"Error: {e}")
    n = open("data.json", "w")
    json.dump(newData, n)
    print(newData)

