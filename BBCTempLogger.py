import requests
from bs4 import BeautifulSoup

# Writes to file in form:
# day,month,year,location,title_time,title_temp(*c),time,temp(*c),direction,wind_speed(mph),humidity(%),pressure(mb)

# Set Desired Location Here
locations = ["2648579", "2650225"]

month_conversions = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5,
                     "Jun":6, "Jul":7, "Aug":8, "Sept":9, "Oct":10,
                     "Nov":11, "Dec":12}

#converts month string to int
def convertMonth(month):
    return month_conversions[month]


# returns string of data to be written for the given location
def getData(location):
    try:
        # Get request on url for rss
        rss_url = "http://open.live.bbc.co.uk/weather/feeds/en/"+location+"/observations.rss"
        response = requests.get(rss_url)
        soup = BeautifulSoup(response.content, features="xml")

        title = soup.find("title")
        location_name = " ".join(title.text.split()[5:-2])
        location_name = location_name[:-1]
        items = soup.find("item")
        titleSplit = items.title.text.split()
        title_time = titleSplit[2]
        title_temp = titleSplit[-2]
        date = items.pubDate.text.split()[1:4]
        day = date[0]
        month = convertMonth(date[1])
        year = date[2]
        time = " ".join(items.pubDate.text.split()[4:])
        description_split = items.description.text.split(',')
        temperature = description_split[0].split()[-2]
        wind_direction = "-".join(description_split[1].split()[2:])
        wind_speed = description_split[2].split()[-1]
        humidity = description_split[3].split()[-1]
        pressure = description_split[4].split()[-1]
        first_half = str(day) + ',' + str(month) + ',' + str(year) + ',' + location_name + ',' +  title_time + ',' + title_temp[:-2] + ','
        second_half = time + ',' + temperature[:-2] + ',' + wind_direction + ',' + wind_speed[:-3] + ',' + humidity[:-1] + ',' + pressure[:-2] +"\n"
        return first_half + second_half

    except:
        return "Failed to retrieve data\n"


f = open("weatherData.txt", "a+")

for location in locations:
    f.write(getData(location))

f.close()
