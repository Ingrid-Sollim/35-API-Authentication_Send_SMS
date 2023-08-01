import requests

api_key="fb6ad1ed94f05b400411a8f9414bce52"
lat =-1.343154
long = -48.454308
exc="current,minutely,daily"

try:
    url="https://api.openweathermap.org/data/2.5/forecast"
    parameters = {"lat":lat,"lon":long,"appid":api_key}
    response = requests.get(url=url,params=parameters)
    print(response.status_code)
    data = response.json()
    #print(data)

except requests.exceptions.RequestException as e:
    print("Error occurred:", e)