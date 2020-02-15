from pytube import YouTube
from bs4 import BeautifulSoup
import requests

SAVE_PATH = 'E:/'
search = "https://www.youtube.com/results"

video_search = input("Type the name of the video: ")
params ={"search_query": video_search}

r = requests.get(search, params=params, verify= False)
soup = BeautifulSoup(r.text, 'html.parser')
result = soup.find('a',{'aria-hidden': 'true'})
link = result['href']

yt = YouTube('http://www.youtube.com' + link)

first_video = yt.streams.filter(progressive=True, subtype = 'mp4').first()

try:
    print('Downloading ', first_video.title)
    first_video.download(SAVE_PATH)
except:
    print("Error downloading")

print(first_video + ' download complete. ')

