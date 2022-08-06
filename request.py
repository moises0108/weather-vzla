import requests
def get_data():

    lat=10.20758912438224
    lon=-67.99113389571072
    APIkey="DYQYURSY247PU6LFDKLUA588Z"
    url='https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{},{}?key={}&unitGroup=metric&include=days'.format(lat,lon,APIkey)
    res=requests.get(url)
    data=res.json()

    clean_data={}
    counter=0
    for element in data["days"]:
        clean_data[counter]=element["temp"]
        counter+=1
    return clean_data
