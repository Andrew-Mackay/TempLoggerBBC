import requests
from bs4 import BeautifulSoup

# Set Desired Location Here
locationID = "2648579"

# Get request on url for rss
rss_url = "http://open.live.bbc.co.uk/weather/feeds/en/"+locationID+"/observations.rss"
response = requests.get(rss_url)


soup = BeautifulSoup(response.content, features="xml")
items = soup.find("item")
print(items.title.text)
print(items.description.text)
print(items.pubDate.text)
