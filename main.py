# import requests
# from bs4 import BeautifulSoup
# url = "https://www.youtube.com/@SamayRainaOfficial/about"


# headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
#     }

# data = requests.get(url=url, headers=headers)



# t = data.text
# soup = BeautifulSoup(t,'html.parser')

# d = soup.prettify()

# print(d)
# with open('index.html', 'w', encoding='utf-8') as file:
#     file.write(d)

   
# import requests
# from bs4 import BeautifulSoup

# url = "https://www.youtube.com/@SamayRainaOfficial/videos"

# headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
#     }

# data = requests.get(url, headers=headers)



# t = data.text
# soup = BeautifulSoup(t,'html.parser')

# d = soup.prettify()
# all_tags = soup.find_all(True)
# tag_count = len(all_tags)

# tag = soup.find("yt-content-metadata-view-model")

# print(tag)

############### Approch - 2 ##############################




from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.youtube.com/@SamayRainaOfficial/about")

title = driver.title
print(title)

# tag = driver.find_elements(By.CLASS_NAME, "ytd-about-channel-renderer")
# print(len(tag))

# ntag = tag.find_elements(By.TAG_NAME, "td")
# for i in nstag:
#     print(i.text)

videos = driver.find_element(By.XPATH, "/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-engagement-panel-section-list-renderer/div[2]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-about-channel-renderer/div/div[5]/table/tbody/tr[5]/td[2]")
tVideo = videos.text.split(" ")
nVideos = int(tVideo[0])
print(type(nVideos))

with open("no_of_videos", "w") as f:
    f.write(nVideos)


driver.quit()