# # import requests
# # from bs4 import BeautifulSoup
# # url = "https://www.youtube.com/@SamayRainaOfficial/about"


# # headers = {
# #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# #     }

# # data = requests.get(url=url, headers=headers)



# # t = data.text
# # soup = BeautifulSoup(t,'html.parser')

# # d = soup.prettify()

# # print(d)
# # with open('index.html', 'w', encoding='utf-8') as file:
# #     file.write(d)

   
# # import requests
# # from bs4 import BeautifulSoup

# # url = "https://www.youtube.com/@SamayRainaOfficial/videos"

# # headers = {
# #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# #     }

# # data = requests.get(url, headers=headers)



# # t = data.text
# # soup = BeautifulSoup(t,'html.parser')

# # d = soup.prettify()
# # all_tags = soup.find_all(True)
# # tag_count = len(all_tags)

# # tag = soup.find("yt-content-metadata-view-model")

# # print(tag)

# ############### Approch - 2 ##############################




# from selenium import webdriver
# from selenium.webdriver.common.by import By

# from selenium.webdriver.support.wait import WebDriverWait
# import json
# driver = webdriver.Chrome()

# driver.get("https://www.youtube.com/@SamayRainaOfficial/about")

# title = driver.title
# print(title)

# # tag = driver.find_elements(By.CLASS_NAME, "ytd-about-channel-renderer")
# # print(len(tag))

# # ntag = tag.find_elements(By.TAG_NAME, "td")
# # for i in nstag:
# #     print(i.text)
# # videos = driver.find_element(By.XPATH, "/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-engagement-panel-section-list-renderer/div[2]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-about-channel-renderer/div/div[5]/table/tbody/tr[5]/td[2]")
# text = ""
# try:
#     element = wait.until(EC.presence_of_element_located(
#             (By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-tabbed-page-header/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/div/div[2]/yt-page-header-renderer/yt-page-header-view-model/div/div[1]/div/yt-content-metadata-view-model/div[2]/span[3]/span")
#         ))
#     video_count = element.text.split(" ")[0]
#     print(video_count)
# finally:
#     driver.quit()
# # tVideo = videos.text.split(" ")
# # nVideos = int(tVideo[0])
# # print(type(nVideos))

# # with open("data.json", "w") as f:
# #     data = json.load(f)

# # print(data)
# # with open("no_of_videos", "w") as f:

# #     if 
# #     f.write(nVideos)


# driver.quit()


import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    n = open("data.json", "w")
    json.dump(newData, n)

def sameVideos(channel):
    print(f"Nothing new😢, {channel}")


if __name__ == "__main__":

    data = open("data.json")
    dataJson = json.load(data)
    for d in dataJson:
        print(d)
        channelName = d["channel"]
        channel_url = f"https://www.youtube.com/@{channelName}"
        try:
            video_count = get_video_count(channel_url)
            print(f"The channel has {video_count} videos.")
            initialVideoCount = d["videos"]
            if initialVideoCount < video_count:
                newVideo(video_count, channelName)
            else:
                sameVideos(channelName)
        except Exception as e:
            print(f"Error: {e}")

