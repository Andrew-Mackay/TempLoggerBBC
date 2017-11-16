import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import datetime


weather = pd.read_csv("weatherData.txt", header=None)
weather = np.array(weather.values)

DIRECTION_CONVERSION = {"Northerly":0, "North-North-Easterly":22.5, "North-Easterly":45,
                        "East-North-Easterly":67.5, "Easterly":90, "East-South-Easterly":112.5,
                        "South-Easterly":135, "South-South-Easterly":157.5, "Southerly":180,
                        "South-South-Westerly":202.5, "South-Westerly":225, "West-South-Westerly":247.5,
                        "Westerly":270, "West-North-Westerly":292.5, "North-Westerly":315.0, "North-North-Westerly":337.5}

glasgow = weather[np.where(weather[:,3] == "Glasgow")]
edinburgh = weather[np.where(weather[:,3] == "Edinburgh")]

# get date values
dates = weather[np.where(weather[:,3] == "Glasgow")][:,0:3]
# swap days and years
dates[:, 0], dates[:, 2] = dates[:, 2], dates[:, 0].copy()
# convert to datetime
x_date = [datetime.datetime(*x).date() for x in dates]

#day, month, year, Location, title_time, title_temp(°C), Server_time, temp(°C),
#direction, wind_speed(mph), humidity(%), pressure(mb)


def plotTemperature():
    glasgow_t = glasgow[:,5]
    edinburgh_t = edinburgh[:,5]
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(x_date, glasgow_t, label="Glasgow")
    ax.plot(x_date, edinburgh_t, label="Edinburgh")
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (°C)")
    ax.legend()
    ax.grid(True)
    ax.legend()
    plt.show()


def convertDirection(direction):
    return DIRECTION_CONVERSION[direction]


def plotWindSpeed(location):
    location_speed = location[:,9]
    location_direction = location[:,8]

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1, projection='polar')
    ax.scatter(np.radians(direction), speed, s=15)
    ax.set_title("Polar plot of wind speed in Las Vegas, 2000-2017")
    ax.set_xlabel("Direction (degrees)")
    ax.set_ylabel("Speed (mph)")


def plotHumidity():
    glasgow_h = glasgow[:,10]
    edinburgh_h = edinburgh[:,10]
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(x_date, glasgow_h, label="Glasgow")
    ax.plot(x_date, edinburgh_h, label="Edinburgh")
    ax.set_xlabel("Date")
    ax.set_ylabel("Humidity (%)")
    ax.legend()
    ax.grid(True)
    ax.legend()
    plt.show()


def plotPressure():
    glasgow_p = glasgow[:,11]
    edinburgh_p = edinburgh[:,11]
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(x_date, glasgow_p, label="Glasgow")
    ax.plot(x_date, edinburgh_p, label="Edinburgh")
    ax.set_xlabel("Date")
    ax.set_ylabel("Pressure (mb)")
    ax.legend()
    ax.grid(True)
    ax.legend()
    plt.show()

plotTemperature()
plotHumidity()
plotPressure()
