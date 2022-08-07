import requests 
import config
from datetime import datetime


def clean_data(info):
    def wrapper():
        data=info()
        clean={}
        lowest=[300,0]
        maximun=[-300,0]
        for element in data["days"]:
            date_time=datetime.strptime(element["datetime"],'%Y-%m-%d').date()
            clean[date_time]=element["temp"]
            lowest=lower(lowest,element["tempmin"],date_time)
            maximun=highest(maximun,element["tempmax"],date_time)
        return clean,lowest,maximun
    return wrapper

@clean_data
def get_data():
     
    lat=10.208268200545701
    lon=-68.00904568708638
    url='https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{},{}?key={}&unitGroup=metric&include=days'.format(lat,lon,config.api_key)
    res=requests.get(url)
    data=res.json()
    return data


def lower(lowest,number,date):
    if  lowest[0]!=min(lowest[0],number):
        lowest[0]=min(lowest[0],number)
        lowest[1]=date
    return lowest

def highest(highest,number,date):
    if  highest[0]!=max(highest[0],number):
        highest[0]=max(highest[0],number)
        highest[1]=date
    return highest