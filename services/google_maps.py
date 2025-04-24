import requests,os
def get_SO2_levels(lat, lng):
    api_key = "4084dee637f1cb29b0124ce90904d9c9"
    url = "http://api.openweathermap.org/data/2.5/air_pollution"
    params = {
        "lat": lat,
        "lon": lng,
        "appid": api_key
    }

    res = requests.get(url, params=params)
    res.raise_for_status()
    return res.json()

def get_directions(source, destination):
    api_key = "AIzaSyAg3FyW8z4g-XJQhwoH-pbC2tlFa8c7Crk"
    url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {
        "origin": source,
        "destination": destination,
        "key": api_key
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
def get_air_quality(lat, lng):
    api_key = "AIzaSyAg3FyW8z4g-XJQhwoH-pbC2tlFa8c7Crk"
    url = f"https://airquality.googleapis.com/v1/currentConditions:lookup?key={api_key}"

    body = {
        "location": {
            "latitude": lat,
            "longitude": lng
        }
    }
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, json=body, headers=headers)
    response.raise_for_status()
    return response.json()
