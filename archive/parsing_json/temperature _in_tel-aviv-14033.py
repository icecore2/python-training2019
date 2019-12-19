# http://lifemichael.com/moodle/mod/assign/view.php?id=14033

# Example link of API:
# api.openweathermap.org/data/2.5/weather?q=London
"""
import urllib.request
ob = urllib.request.urlopen('https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22')
print(ob.read())
"""
# Global things
from urllib import request
import json

api_key = "01349560e811e5b713d01174e05d4a90"
city = "tel%20aviv"  # "Tel Aviv"


def firstTry(city, api_key):
    # issue 1: TypeError: Object of type HTTPResponse is not JSON serializable

    ob = request.urlopen('https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}'.format(city, api_key))
    data = ob.read()

    weather_dict = json.loads(data)
    # coordinates, weather, description, base, main  = [weather_result]
    print("weather_dict:", weather_dict)
# TODO: finish this
    for item in weather_dict:
        if weather_dict[item] == 'name':
            print(weather_dict[item])


firstTry(city,api_key)


def secondTry(city, api_key):
    url = request.urlopen('https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}'.format(city, api_key))
    ob = json.load(url)

    # print("ob.read():", ob.read()) <=== ob.read() did issue here.
    # print("ob.read():", ob)

    weather = ob
    if weather['cod'] == 200:
        for item in weather:
            if item == 'name':
                print("City:", weather['name'])
            if item == 'main':
                print("Temperature in {}:".format(weather['name']), int(((weather['main']['temp'] - 32) * 5 / 9)))
            # print(weather[item])

    else:
        print("Code error:", weather['cod'])

# secondTry(city, api_key)
