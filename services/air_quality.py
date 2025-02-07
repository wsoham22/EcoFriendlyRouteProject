import requests

def get_aqi_data(source, destination):
    aqi_api_url = f"https://api.openaq.org/v1/latest?coordinates={source}"
    response = requests.get(aqi_api_url)
    return response.json()
