from flask import Flask, jsonify, request
from flask_cors import CORS
import math
from graph import CityGraph
from algorithms import dijkstra, astar, compare_algorithms

app = Flask(__name__)
CORS(app)

# Initialize the graph
city = CityGraph()
city.build_real_ludhiana() # <-- Changed to the new OSM function

def serialize_result(result: dict) -> dict:
    return {
        "path": result.get("path", []),
        "total_distance": round(result.get("total_distance", 0), 2),
        "total_time": round(result.get("total_time", 0), 2),
        "nodes_visited": result.get("nodes_visited", 0),
        "found": result.get("found", False),
    }

def get_nearest_node(lat: float, lng: float) -> str:
    """Snaps a random GPS coordinate to the nearest known graph node using Haversine."""
    def haversine(lat1, lon1, lat2, lon2):
        R = 6371.0
        dlat, dlon = math.radians(lat2 - lat1), math.radians(lon2 - lon1)
        a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
        return R * (2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)))

    nodes = city.get_nodes_info()
    nearest = min(nodes, key=lambda n: haversine(lat, lng, n['lat'], n['lng']))
    return nearest['id']

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Route API Live!", "version": "3.1"})

@app.route("/graph-data", methods=["GET"])
def graph_data():
    return jsonify({"nodes": city.get_nodes_info(), "edges": city.get_edges_info()})

@app.route("/route", methods=["POST"])
def find_route():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    algorithm = data.get("algorithm", "both").lower()

    try:
        # Snap map clicks to the nearest road node
        if "source_coords" in data:
            source = get_nearest_node(data["source_coords"]["lat"], data["source_coords"]["lng"])
        else:
            source = data.get("source", "").strip()

        if "dest_coords" in data:
            destination = get_nearest_node(data["dest_coords"]["lat"], data["dest_coords"]["lng"])
        else:
            destination = data.get("destination", "").strip()
    except Exception as e:
        return jsonify({"error": f"Failed to process coordinates: {str(e)}"}), 400

    if not source or not destination:
        return jsonify({"error": "Missing source or destination"}), 400
        
    if source == destination:
        return jsonify({"error": "Source and destination are too close! They snapped to the same intersection."}), 400

    graph = city.graph
    response = {"source": source, "destination": destination}

    if algorithm in ("dijkstra", "both"):
        response["dijkstra"] = serialize_result(dijkstra(graph, source, destination))

    if algorithm in ("astar", "both"):
        coords = city.get_coordinates()
        response["astar"] = serialize_result(astar(graph, source, destination, coords))

    if algorithm == "both":
        response["comparison"] = compare_algorithms(response["dijkstra"], response["astar"])

    return jsonify(response)

@app.route("/update-traffic", methods=["POST"])
def update_traffic():
    data = request.get_json(silent=True) or {}
    intensity = max(0.0, min(1.0, float(data.get("intensity", 0.5))))
    return jsonify({"updated": city.simulate_traffic(intensity), "intensity": intensity})

@app.route("/reset-traffic", methods=["POST"])
def reset_traffic():
    city.reset_traffic()
    return jsonify({"message": "Reset"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)