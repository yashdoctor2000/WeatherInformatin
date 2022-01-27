import requests
from pprint import pprint

API_Key = "fc3899eb9764eaaa9c05d17755fc8a37"
 
city=input("Enter the City name: ")
base_url="http://api.openweathermap.org/data/2.5/forecast?appid="+API_Key+"&q="+city
weather_data=requests.get(base_url).json()

pprint(weather_data)
