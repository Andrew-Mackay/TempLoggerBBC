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

locations = [glasgow, edinburgh]

# get date values
dates = weather[np.where(weather[:,3] == "Glasgow")][:,0:3]
# swap days and years
dates[:, 0], dates[:, 2] = dates[:, 2], dates[:, 0].copy()
# convert to datetime
x_date = [datetime.datetime(*x).date() for x in dates]

#day, month, year, Location, title_time, title_temp(°C), Server_time, temp(°C),
#direction, wind_speed(mph), humidity(%), pressure(mb)


def plotTemperature():
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    for location in locations:
        ax.plot(x_date, location[:,5], label=location[0,3])

    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (°C)")
    ax.legend()
    ax.grid(True)
    ax.legend()
    plt.show()


def plotPolarWindSpeed(location):
    city = location[0,3]
    location_s = location[:,9].tolist()
    location_d = location[:,8].tolist()
    # convert direction to radians
    for i in range(len(location_d)):
        location_d[i] = np.deg2rad(DIRECTION_CONVERSION[location_d[i]])
    ax = plt.subplot(111, projection='polar')
    ax.scatter(location_d, location_s)
    ax.set_theta_direction(-1)
    ax.set_theta_zero_location("N")
    ax.set_title("Polar plot of wind speed in " + city)
    ax.set_xlabel("Direction (degrees)")
    ax.set_ylabel("Speed (mph)")
    ax.grid(True)
    plt.show()


def plotWindSpeed():
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    for location in locations:
        ax.plot(x_date, location[:,9], label=location[0,3])

    ax.set_xlabel("Date")
    ax.set_ylabel("Wind Speed (mph)")
    ax.legend()
    ax.grid(True)
    ax.legend()
    plt.show()


def plotHumidity():
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    for location in locations:
        ax.plot(x_date, location[:,10], label=location[0,3])
    ax.set_xlabel("Date")
    ax.set_ylabel("Humidity (%)")
    ax.legend()
    ax.grid(True)
    ax.legend()
    plt.show()


def plotPressure():
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    for location in locations:
        ax.plot(x_date, location[:,11], label=location[0,3])
    ax.set_xlabel("Date")
    ax.set_ylabel("Pressure (mb)")
    ax.legend()
    ax.grid(True)
    ax.legend()
    plt.show()


def showOptions():
    print("Options: ")
    print("\t 1: Temperature")
    print("\t 2: Wind Speed")
    print("\t 3: Humidity")
    print("\t 4: Pressure")
    print("\t 5: Polar Plot of Wind Speed")
    print("\t o: display options")
    print("\t q: quit")

showOptions()
option = ""
while option != 'q':
    option = input("Select option: ")
    if option == '1':
        plotTemperature()

    elif option == '2':
        plotWindSpeed()

    elif option == '3':
        plotHumidity()

    elif option == '4':
        plotPressure()

    elif option == '5':
        for location in locations:
            plotPolarWindSpeed(location)

    elif option == 'o':
        showOptions()
