import networkx as nx
import random
import osmnx as ox  # NEW: OpenStreetMap library

class CityGraph:
    def __init__(self):
        self.graph = nx.DiGraph()
        self._base_weights: dict[tuple, float] = {}
        self._coords: dict[str, tuple[float, float]] = {}

    def add_location(self, name: str, lat: float, lng: float):
        self.graph.add_node(name, lat=lat, lng=lng)
        self._coords[name] = (lat, lng)

    def add_road(self, u: str, v: str, distance: float, speed_kmh: float = 40.0, bidirectional: bool = True):
        traffic_factor = 1.0
        weight = distance * traffic_factor
        attrs = {
            "base_distance":  distance,
            "traffic_factor": traffic_factor,
            "weight":         weight,
            "speed_kmh":      speed_kmh,
        }
        self.graph.add_edge(u, v, **attrs)
        self._base_weights[(u, v)] = distance
        if bidirectional:
            self.graph.add_edge(v, u, **attrs)
            self._base_weights[(v, u)] = distance

    def build_real_ludhiana(self):
        """
        Downloads the actual street network of Ludhiana using OpenStreetMap.
        This fetches thousands of real intersections and roads.
        """
        print("🌍 Downloading real Ludhiana road network (this takes 15-30 seconds)...")
        
        # Download a 8km radius around central Ludhiana (covers almost the whole city)
        # Using a bounding radius prevents the server from crashing with too much data
        center_point = (30.900965, 75.857275) 
        G_osm = ox.graph_from_point(center_point, dist=8000, network_type="drive")
        
        print(f"✅ Downloaded {len(G_osm.nodes)} nodes and {len(G_osm.edges)} edges!")

        # 1. Convert OSM nodes to our graph
        for node_id, data in G_osm.nodes(data=True):
            # OSM uses 'y' for lat and 'x' for lng
            self.add_location(str(node_id), lat=data['y'], lng=data['x'])

        # 2. Convert OSM roads to our graph
        for u, v, key, data in G_osm.edges(keys=True, data=True):
            # OSM provides length in meters, convert to km
            dist_km = data.get('length', 100) / 1000.0
            
            # Extract speed limit if available, otherwise default to 40 km/h
            speed = 40.0
            if 'maxspeed' in data:
                ms = data['maxspeed']
                if isinstance(ms, list): speed = float(ms[0])
                elif isinstance(ms, str) and ms.isdigit(): speed = float(ms)
            
            # OSMnx already handles one-way vs two-way streets by providing the proper directed edges,
            # so we set bidirectional=False to avoid duplicating roads improperly.
            self.add_road(str(u), str(v), dist_km, speed_kmh=speed, bidirectional=False)

    # --- Traffic Simulation remains exactly the same ---
    def simulate_traffic(self, intensity: float = 0.5) -> int:
        updated = 0
        for u, v, data in self.graph.edges(data=True):
            max_factor = 1.0 + 3.0 * intensity
            factor = random.uniform(1.0, max_factor)
            data["traffic_factor"] = round(factor, 2)
            data["weight"]         = round(data["base_distance"] * factor, 3)
            updated += 1
        return updated

    def reset_traffic(self):
        for u, v, data in self.graph.edges(data=True):
            data["traffic_factor"] = 1.0
            data["weight"]         = data["base_distance"]

    def get_node_names(self) -> list[str]: return list(self.graph.nodes())
    def get_coordinates(self) -> dict[str, tuple[float, float]]: return dict(self._coords)
    def get_nodes_info(self) -> list[dict]: return [{"id": n, "lat": d.get("lat", 0), "lng": d.get("lng", 0)} for n, d in self.graph.nodes(data=True)]
    def get_edges_info(self) -> list[dict]: return [{"source": u, "target": v, "base_distance": d.get("base_distance", 0), "traffic_factor": d.get("traffic_factor", 1.0), "weight": d.get("weight", 0), "speed_kmh": d.get("speed_kmh", 40)} for u, v, d in self.graph.edges(data=True)]