import requests
from bs4 import BeautifulSoup

# Set Desired Location Here
locations = ["2648579", "2650225"]


for location in locations:
    # Get request on url for rss
    rss_url = "http://open.live.bbc.co.uk/weather/feeds/en/"+location+"/observations.rss"
    response = requests.get(rss_url)

    # date, time, location, temp, wind speed, humidity, pressure
    soup = BeautifulSoup(response.content, features="xml")
    title = soup.find("title")
    location_name = title.text.split()[5:-2] # i.e Glasgow

    items = soup.find("item")
    titleSplit = items.title.text.split()
    title_time = titleSplit[2]
    title_temp = titleSplit[-2]
    date = items.pubDate.text.split()[0:4]
    time = items.pubDate.text.split()[4:]
    description_split = items.description.text.split(',')
    temperature = description_split[0].split()[-2]
    wind_direction = description_split[1].split()[2:]
    wind_speed = description_split[2].split()[-1]
    humidity = description_split[3].split()[-1]
    pressure = description_split[4].split()[-1]
    print(" ".join(location_name))
    print("Date:", " ".join(date), "\nTime:", " ".join(time), "\nTitle Time:", title_time, "\nTitle Temp:", title_temp,
          "\nTemp:", temperature, "\nWind Direction:", "-".join(wind_direction), "\nWind Speed:", wind_speed,
          "\nHumidity:", humidity, "\nPressure:", pressure)
    print("----------------------------------------------------------")
    #print(" ".join(date), time, temp)
