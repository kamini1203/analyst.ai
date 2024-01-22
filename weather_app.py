import requests
import json
city=input('enter the name of city:')
url=f"https://api.weatherapi.com/v1/current.json?key=ed3481e001d045b697d143714230208&q={city}"
r=requests.get(url)
weather_data=r.json()
for c1 in weather_data.keys():
    print(c1)
    for c2 in weather_data[c1]:
        print("\t",c2,":",weather_data[c1][c2])
    