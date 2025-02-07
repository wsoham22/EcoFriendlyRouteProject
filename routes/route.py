from flask import Blueprint, jsonify
from flask_socketio import emit
from services.google_maps import get_traffic_data
from services.air_quality import get_aqi_data
from services.terrain import get_terrain_data
from models.load_model import predict_route
from app import socketio

# WebSocket event for real-time route prediction
@socketio.on("predict_route")
def handle_predict_route(data):
    try:
        # Directly access data passed by the client
        source = data["source"]
        destination = data["destination"]

        # Fetch real-time traffic, AQI, and terrain data
        traffic_data = get_traffic_data(source, destination)
        aqi_data = get_aqi_data(source)
        terrain_data = get_terrain_data(source, destination)

        # Predict eco-score using ML model
        prediction = predict_route(source, destination, traffic_data, aqi_data, terrain_data)

        # Send the prediction result back via WebSocket
        emit("route_update", {
            "eco_score": prediction,
            "route": "Optimized Route Data"
        })
    except Exception as e:
        # Handle any exceptions and send error via WebSocket
        emit("error", {"message": str(e)})
