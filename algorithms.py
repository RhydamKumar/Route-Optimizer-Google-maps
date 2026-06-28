"""
algorithms.py – Pathfinding Algorithms (GPS Updated)
======================================================
"""

import heapq
import math
import time
from typing import Optional

# ══════════════════════════════════════════════════════════════════════════════
# 1.  DIJKSTRA'S ALGORITHM
# ══════════════════════════════════════════════════════════════════════════════

def dijkstra(graph, source: str, destination: str) -> dict:
    start_time = time.perf_counter()

    dist = {node: float("inf") for node in graph.nodes()}
    dist[source] = 0.0
    prev: dict[str, Optional[str]] = {node: None for node in graph.nodes()}
    heap = [(0.0, source)]
    visited: set[str] = set()
    nodes_visited = 0

    while heap:
        current_cost, current_node = heapq.heappop(heap)

        if current_node in visited:
            continue
        visited.add(current_node)
        nodes_visited += 1

        if current_node == destination:
            break

        for neighbor in graph.successors(current_node):
            edge_data  = graph[current_node][neighbor]
            edge_cost  = edge_data.get("weight", 1.0)
            new_cost   = current_cost + edge_cost

            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                prev[neighbor] = current_node
                heapq.heappush(heap, (new_cost, neighbor))

    path = _reconstruct_path(prev, source, destination)
    total_distance = dist[destination] if dist[destination] != float("inf") else 0
    total_time = _estimate_time(graph, path)
    elapsed_ms = (time.perf_counter() - start_time) * 1000

    return {
        "path":           path,
        "total_distance": round(total_distance, 2),
        "total_time":     total_time,
        "nodes_visited":  nodes_visited,
        "found":          bool(path),
        "elapsed_ms":     round(elapsed_ms, 4),
        "algorithm":      "Dijkstra",
    }

# ══════════════════════════════════════════════════════════════════════════════
# 2.  A* ALGORITHM
# ══════════════════════════════════════════════════════════════════════════════

def astar(graph, source: str, destination: str, coords: dict[str, tuple[float, float]]) -> dict:
    start_time = time.perf_counter()

    def haversine(a: str, b: str) -> float:
        """Real-world distance between two lat/lng points in km (Spherical)."""
        lat1, lon1 = coords.get(a, (0, 0))
        lat2, lon2 = coords.get(b, (0, 0))
        R = 6371.0 # Earth radius in km
        
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        
        val = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(val), math.sqrt(1 - val))
        return R * c

    g_score = {node: float("inf") for node in graph.nodes()}
    g_score[source] = 0.0

    f_score = {node: float("inf") for node in graph.nodes()}
    f_score[source] = haversine(source, destination)

    prev: dict[str, Optional[str]] = {node: None for node in graph.nodes()}
    heap = [(f_score[source], source)]
    visited: set[str] = set()
    nodes_visited = 0

    while heap:
        _, current_node = heapq.heappop(heap)

        if current_node in visited:
            continue
        visited.add(current_node)
        nodes_visited += 1

        if current_node == destination:
            break

        for neighbor in graph.successors(current_node):
            edge_data = graph[current_node][neighbor]
            edge_cost = edge_data.get("weight", 1.0)
            tentative_g = g_score[current_node] + edge_cost

            if tentative_g < g_score[neighbor]:
                prev[neighbor]    = current_node
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + haversine(neighbor, destination)
                heapq.heappush(heap, (f_score[neighbor], neighbor))

    path = _reconstruct_path(prev, source, destination)
    total_distance = g_score[destination] if g_score[destination] != float("inf") else 0
    total_time = _estimate_time(graph, path)
    elapsed_ms = (time.perf_counter() - start_time) * 1000

    return {
        "path":           path,
        "total_distance": round(total_distance, 2),
        "total_time":     total_time,
        "nodes_visited":  nodes_visited,
        "found":          bool(path),
        "elapsed_ms":     round(elapsed_ms, 4),
        "algorithm":      "A*",
    }

# ══════════════════════════════════════════════════════════════════════════════
# 3.  COMPARISON HELPER
# ══════════════════════════════════════════════════════════════════════════════

def compare_algorithms(d_result: dict, a_result: dict) -> dict:
    d_dist  = d_result.get("total_distance", 0)
    a_dist  = a_result.get("total_distance", 0)
    d_nodes = d_result.get("nodes_visited", 0)
    a_nodes = a_result.get("nodes_visited", 0)

    dist_diff = round(abs(d_dist - a_dist), 3)
    same_path = d_result.get("path") == a_result.get("path")
    nodes_saved = d_nodes - a_nodes
    efficiency_pct = round((nodes_saved / d_nodes * 100) if d_nodes else 0, 1)

    return {
        "same_path":          same_path,
        "dijkstra_distance":  d_dist,
        "astar_distance":     a_dist,
        "distance_diff":      dist_diff,
        "dijkstra_nodes":     d_nodes,
        "astar_nodes":        a_nodes,
        "nodes_saved_by_astar": nodes_saved,
        "astar_efficiency_pct": efficiency_pct,
        "verdict": (
            f"A* explored {nodes_saved} fewer nodes ({efficiency_pct}% more efficient). "
            + ("Both found identical paths." if same_path else f"Path distance differs by {dist_diff} km.")
        ),
    }

# ══════════════════════════════════════════════════════════════════════════════
# 4.  UTILITIES
# ══════════════════════════════════════════════════════════════════════════════

def _reconstruct_path(prev: dict, source: str, destination: str) -> list[str]:
    path = []
    node: Optional[str] = destination
    while node is not None:
        path.append(node)
        node = prev.get(node)
        if node == source:
            path.append(source)
            break
    else:
        return []
    path.reverse()
    if not path or path[0] != source or path[-1] != destination:
        return []
    return path

def _estimate_time(graph, path: list[str]) -> float:
    if len(path) < 2:
        return 0.0
    total_minutes = 0.0
    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]
        if graph.has_edge(u, v):
            dist   = graph[u][v].get("weight", 1.0)
            speed  = graph[u][v].get("speed_kmh", 40.0)
            total_minutes += (dist / speed) * 60
    return round(total_minutes, 1)