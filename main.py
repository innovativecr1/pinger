# import requests
# from bs4 import BeautifulSoup
# # url = "https://www.youtube.com/@SamayRainaOfficial/videos"
# url = "/index.html"

# data = requests.get(url)

# t = data.text
# soup = BeautifulSoup(t,'html.parser')

# d = soup.prettify()

# print(d)
# # with open('index.html', 'w', encoding='utf-8') as file:
# #     file.write(d)

   
import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/@SamayRainaOfficial/videos"
data = requests.get(url)

t = data.text
soup = BeautifulSoup(t,'html.parser')

d = soup.prettify()
all_tags = soup.find_all(True)
tag_count = len(all_tags)

tag = soup.find("yt-content-metadata-view-model")

print(tag)