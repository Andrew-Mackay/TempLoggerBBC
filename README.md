# TempLoggerBBC
Script written in Python 3 that logs weather data from http://www.bbc.co.uk/weather/.
The script writes the data to a file called "weatherData.txt".
The format of the output is as followed:
day,month,year,location,title_time,title_temp(°C),time,temp(°C),direction,wind_speed(mph),humidity(%),pressure(mb)
To specify the locations you want to log, open up BBCTempLogger.py in a text editor and change the locations array.
A cron file is also included to run this script every day at 12:00.

Install python3-lxml by running:
    sudo apt-get install python3-lxml -y
    
Install requirements by running:
    pip3 install -r requirements.txt
    
Add crontab by running:
    crontab templogger.cron
    
Execute script manually by running:
    python3 BBCTempLogger.py
