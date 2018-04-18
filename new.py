import json
import urllib.request as ur
city = input("Please enter a city name: ")
url = "https://www.metaweather.com/api/location/search/?query="+city
data = ur.urlopen(url).read()
readable_json = json.loads(data)
woeid = 0
for i in readable_json:
    woeid = i['woeid']
if woeid != 0:    
    weather_url = "https://www.metaweather.com/api/location/"+str(woeid)
    data = ur.urlopen(weather_url).read()
    readable_json = json.loads(data)
    consolidated_weather = readable_json['consolidated_weather']
    count = 1
    for i in consolidated_weather:
        if count == 1:            
            print(round(i['min_temp'],0))
            print(round(i['max_temp']),0)
            count = 2
        
            
            


