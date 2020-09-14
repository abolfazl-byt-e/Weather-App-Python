import requests
import json

api_key = "9583532257be6961a4501aefc6f17c10"
city = input("enter city:\n")
url = "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s" %(city, api_key)
r = requests.get(url)
data = r.text
data = json.loads(data) 
# print(data)
def ftc(f):
    ## convert fahrenheit to celcus
    c = (f - 32) * 5 / 9
    return c
print(data["name"], data["sys"]["country"], data["weather"][0]["description"],ftc(data["main"]["temp"]), sep=" | ")