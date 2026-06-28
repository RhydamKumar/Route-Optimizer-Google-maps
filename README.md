# 🗺️ Route Optimizer using Google Maps API

A lightweight route optimization application that computes the shortest path using **Dijkstra's Algorithm** and **A* Search Algorithm** while using **Google Maps JavaScript API** only as the map visualization layer.

Unlike traditional navigation applications that rely on paid routing APIs, this project performs all shortest-path computations locally using custom graph algorithms written in Python. It is designed primarily for students, researchers, and developers who want to experiment with routing algorithms without incurring API usage costs.

---

# 📑 Table of Contents

* Overview
* Why This Project?
* How This Project Works
* Features
* Current Limitation
* Project Architecture
* Project Structure
* Technologies Used
* Installation
* Usage
* Algorithms
* Educational Objectives
* Future Improvements
* Contributing
* License

---

# 📖 Overview

Route optimization is one of the most fundamental problems in computer science and modern navigation systems. Applications such as Google Maps solve this problem extremely well, but integrating their routing services into your own application generally requires using paid APIs.

This project demonstrates an alternative educational approach by separating **map visualization** from **route computation**.

Instead of requesting routes from Google's servers, this application:

* Displays the map using Google Maps JavaScript API.
* Builds its own graph representation.
* Computes shortest paths locally using Python.
* Displays the computed route on the map.

The project combines concepts from:

* Graph Theory
* Shortest Path Algorithms
* Web Development
* Flask
* Google Maps Integration

making it an excellent learning resource for students and developers.

---

# ❓ Why This Project?

A common question is:

> **"Why use this project when Google Maps already exists?"**

The answer is that Google Maps itself is a free application for users, but developers who want to build applications using Google's routing services generally need to use APIs such as the Directions API or Routes API, which are paid based on usage.

For many people, especially:

* 🎓 Students
* 🔬 Researchers
* 💻 Developers building prototypes
* 📚 People learning graph algorithms

these costs are unnecessary because they simply want to experiment with routing algorithms or build academic projects.

This project provides a free educational alternative by implementing the routing logic independently.

Instead of paying for route calculations, users only need a Google Maps JavaScript API key to display the map interface, while the shortest path itself is computed entirely by the project's own algorithms.

---

# ⚙️ How Does It Work?

Google provides several APIs for route optimization, but those services perform the path computation on Google's servers and are billed according to API usage.

This project follows a different approach.

1. Display the map using the Google Maps JavaScript API.
2. Create a graph representing roads and intersections.
3. Execute Dijkstra's Algorithm or A* Search locally in Python.
4. Compute the shortest path without calling Google's routing APIs.
5. Visualize the resulting path on Google Maps.

In simple terms:

**Google provides the map interface.**

**This project provides the route calculation.**

Because the routing logic runs entirely on your own system, no paid routing API is required.

To run the project, generate your own Google Maps JavaScript API key from Google Cloud Console and replace the placeholder API key in the project.

---

# ✨ Features

* 🌍 Interactive Google Maps interface
* 📍 Source and destination selection
* 🛣️ Shortest path computation
* ⚡ Dijkstra's Algorithm implementation
* 🚀 A* Search Algorithm implementation
* 🧠 Graph-based routing
* 🔄 Flask backend
* 📊 Interactive frontend
* 🎓 Educational implementation of graph algorithms
* 💰 No dependency on paid routing APIs
* 🧩 Easy to extend for additional locations

---

# ⚠️ Current Limitation

At present, the project contains graph data only for **Ludhiana, Punjab**.

This limitation is intentional.

Generating graph data for larger geographical regions requires considerably more memory and computational resources. Since the project was developed and tested on a low-end computer, limiting the graph to a single city ensures smooth local execution and faster algorithm performance.

This limitation is **not** imposed by the algorithms themselves.

Anyone with a more capable system can easily expand the project by:

* Adding graph data for additional cities
* Increasing the geographical coverage
* Modifying the graph generation code
* Creating larger graph datasets

The routing algorithms will continue to work without modification once the graph is expanded.

---

# 🏗️ Project Architecture

```text
                User
                  │
                  ▼
           index.html
                  │
                  ▼
Google Maps JavaScript API
                  │
                  ▼
          Flask Backend
             (app.py)
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
 algorithms.py         graph.py
        │
        ▼
Shortest Path Algorithms
        │
        ▼
 Optimized Route
        │
        ▼
Displayed on Google Maps
```

---

# 📁 Project Structure

```text
Route-Optimizer-Google-maps/
│
├── app.py                 # Flask backend
├── algorithms.py          # Dijkstra & A* implementations
├── graph.py               # Graph representation
├── index.html             # Frontend interface
└── README.md
```

---

# 💻 Technologies Used

## Frontend

* HTML5
* CSS3
* JavaScript
* Google Maps JavaScript API

## Backend

* Python
* Flask

## Algorithms

* Dijkstra's Algorithm
* A* Search Algorithm

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/RhydamKumar/Route-Optimizer-Google-maps.git
```

## Navigate to the Project

```bash
cd Route-Optimizer-Google-maps
```

## Install Dependencies

```bash
pip install flask
```

## Configure Google Maps

Generate a Google Maps JavaScript API key from the Google Cloud Console.

Replace the placeholder API key inside the project with your own API key.

## Run the Application

```bash
python app.py
```

Open the URL displayed by Flask in your browser.

---

# 🚀 Usage

1. Launch the Flask server.
2. Open the application in your browser.
3. Select the source location.
4. Select the destination.
5. Execute the routing algorithm.
6. View the optimized route displayed on Google Maps.

---

# 🧮 Algorithms Implemented

## Dijkstra's Algorithm

Dijkstra's Algorithm guarantees the shortest path in weighted graphs with non-negative edge weights.

### Characteristics

* Complete
* Optimal
* Reliable
* Widely used in routing applications

---

## A* Search Algorithm

A* Search improves performance by using heuristics to prioritize promising paths.

### Characteristics

* Faster search in many practical scenarios
* Heuristic-based optimization
* Optimal when using an admissible heuristic
* Commonly used in modern navigation systems

---

# 🎓 Educational Objectives

This project demonstrates practical implementation of:

* Graph Theory
* Pathfinding Algorithms
* Flask Web Development
* Google Maps Integration
* Frontend-Backend Communication
* Route Visualization
* Algorithm Design

---

# 🚀 Future Improvements

* Support multiple cities
* Automatic graph generation
* Execution time comparison
* Alternative route suggestions
* Traffic-aware routing
* Better UI/UX
* Cloud deployment
* Larger graph datasets
* Route caching for improved performance

---

# 🤝 Contributing

Contributions are always welcome.

Feel free to fork the repository, improve the implementation, and submit a Pull Request.

---

# 📜 License

This project is intended for educational, research, and learning purposes.

You are welcome to use, modify, and extend the project while providing appropriate credit to the original repository.

---

# 👨‍💻 Author

**Rhydam Kumar**

GitHub: https://github.com/RhydamKumar

---

⭐ If you found this project useful or learned something from it, consider giving it a **Star** on GitHub!
