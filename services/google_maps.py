import requests
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def get_traffic_data(source, destination):
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={source}&destination={destination}&key={GOOGLE_MAPS_API_KEY}"
    response = requests.get(url)
    return response.json()
