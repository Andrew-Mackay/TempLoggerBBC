import requests
from bs4 import BeautifulSoup

# Set Desired Location Here
locations = ["2648579"]


for location in locations:
    # Get request on url for rss
    rss_url = "http://open.live.bbc.co.uk/weather/feeds/en/"+location+"/observations.rss"
    response = requests.get(rss_url)

    # date, time, location, temp, wind speed, humidity, pressure
    soup = BeautifulSoup(response.content, features="xml")
    title = soup.find("title")
    location_name = title.text.split()[5] # i.e Glasgow

    items = soup.find("item")
    titleSplit = items.title.text.split()
    title_time = titleSplit[2]
    title_temp = titleSplit[-2]
    date = items.pubDate.text.split()[0:4]
    time = items.pubDate.text.split()[4]
    description_split = items.description.text.split(',')
    temperature = description_split[0].split()[-2]
    wind_direction = description_split[1].split()[2:]
    wind_speed = description_split[2].split()[-1]
    humidity = description_split[3].split()[-1]
    pressure = description_split[4].split()[-1]
    print(location_name)
    print("Date:", date, "Time:", time, "Title Time:", title_time, "Title Temp:", title_temp, "\n",
          "Temp:", temperature, "Wind Direction:", wind_direction, "Wind Speed:", wind_speed,"\n",
          "Humidity:", humidity, "Pressure:", pressure)
    #print(" ".join(date), time, temp)
