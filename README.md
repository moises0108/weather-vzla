# weather-avg next 15 days
## Description

take the next 15 days pronostic weather from https://www.visualcrossing.com/weather-api and graph with the warming and coldest day from any location
## Install and Run
- First of all you need to install de packacge in [requeriments.txt](requeriments.txt)
- Create a account in https://www.visualcrossing.com/weather-api and copy the apikey
- Paste the apikey in a new file called config.py like this: api_key="YOUR KEY" 
- if you want to change the coords just modift the variables 'lat'(latitude) and 'lon'(longitude) from th file [request.py](request.py)
- if you want to change de title just change variable 'title' in [graphic.py](graphic.py)
## How to use
- Just run the file main.py and you will se the graph like this
![image](https://user-images.githubusercontent.com/49890569/183305098-a9d50ad6-6155-48f0-a4a1-6491d9d7de65.png)
