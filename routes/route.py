from flask import Blueprint, request, jsonify, render_template, json
from services.google_maps import get_directions,get_air_quality,get_SO2_levels,get_Alldirections
import os
# Create Blueprint
api_routes = Blueprint("api_routes", __name__)

@api_routes.route("/get_directions", methods=["GET"])
def handle_get_directions():
    try:
        source = request.args.get("source")
        destination = request.args.get("destination")

        if not source or not destination:
            return jsonify({"error": "Missing source or destination"}), 400

        directions = get_directions(source, destination)
        return jsonify({"route": directions}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
@api_routes.route("/get_all_directions", methods=["GET"])
def handle_get_all_directions():
    try:
        source = request.args.get("source")
        destination = request.args.get("destination")

        if not source or not destination:
            return jsonify({"error": "Missing source or destination"}), 400

        directions = get_Alldirections(source, destination)
        return jsonify({"route": directions}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
@api_routes.route('/get_aqi_by_coords', methods=['POST'])
def get_aqi_by_coords():
    try:
        lat = request.args.get("lat")
        lng = request.args.get("lng")

        if not lat or not lng:
            return jsonify({"error": "Missing lat or lng"}), 400

        data = get_air_quality(float(lat), float(lng))
        return jsonify({"air_quality": data}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_routes.route('/get_so2', methods=['GET'])
def get_SO2():
    try:
        lat = request.args.get("lat")
        lng = request.args.get("lng")

        if not lat or not lng:
            return jsonify({"error": "Missing lat or lng"}), 400

        data = get_SO2_levels(float(lat), float(lng))
        return jsonify({"air_quality": data}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_routes.route("/show_map")
def show_map():
    try:
        source = request.args.get("source")
        destination = request.args.get("destination")
        # source =  "Mumbai"
        # destination = "Pune"
        if not source or not destination:
                return jsonify({"error": "Missing source or destination"}), 400
        route_data = get_directions(source, destination)
        # Pretty print in terminal
        return render_template("map.html", route_data=json.dumps(route_data))
    except Exception as e:
        return jsonify({"error": str(e)}), 500
