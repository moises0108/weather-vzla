import requests 
import config

def get_data():
    lat=10.20758912438224
    lon=-67.99113389571072

    url='https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{},{}?key={}&unitGroup=metric&include=days'.format(lat,lon,config.api_key)
    res=requests.get(url)
    data=res.json()
    return clean_data(data)


def clean_data(data:dict)->dict:
    clean={}
    counter=0
    lowest=300
    maximun=-300
    for element in data["days"]:
        clean[counter]=element["temp"]
        lowest=min(lowest,element["tempmin"])
        maximun=max(maximun,element["tempmax"])
        counter+=1
    return clean,lowest,maximun


