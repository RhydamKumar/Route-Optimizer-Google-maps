# 🗺️ Route Optimizer using Google Maps API

A web-based route optimization application that computes the shortest path using **Dijkstra's Algorithm** and **A* Search Algorithm**, while leveraging **Google Maps JavaScript API** only for map visualization.

Instead of relying on Google's paid routing services, this project performs all shortest-path calculations locally using Python, making it an affordable solution for students, researchers, and developers who want to experiment with pathfinding algorithms.

---

# 📌 Table of Contents

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
* Algorithms Implemented
* Future Improvements
* Contributing
* License

---

# 📖 Overview

Modern navigation applications like Google Maps provide excellent routing services. However, their routing APIs are paid services, making them less practical for students, researchers, and hobby developers who simply want to experiment with shortest-path algorithms.

This project demonstrates that route optimization can be performed independently using classical graph algorithms while still benefiting from Google's high-quality map interface.

Google Maps is used **only as the visualization layer**. All shortest-path calculations are executed locally using custom implementations of Dijkstra's Algorithm and A* Search Algorithm written in Python.

The project combines:

* Python
* Flask
* HTML
* JavaScript
* Google Maps JavaScript API
* Graph Theory
* Pathfinding Algorithms

to build a lightweight educational routing system.

---

# ❓ Why Use This Project When Google Maps Already Exists?

This is probably the most common question.

The answer is simple.

Google Maps itself is free to use as an application, but if you want to build your own software that uses Google's routing services, you typically need to use paid APIs such as the Directions API or Routes API. For projects with many requests, the cost can increase quickly.

This project is intended for:

* 🎓 Students building academic projects
* 🔬 Researchers testing new routing algorithms
* 💻 Developers creating prototype applications
* 📚 Anyone learning graph algorithms

Instead of paying for routing API requests, this project performs the route computation locally using Python.

You only need a Google Maps JavaScript API key to display the map interface. The shortest-path computation is completely handled by your own implementation.

This makes the project an excellent learning resource and a low-cost alternative for experimentation.

---

# ⚙️ How Does This Project Avoid Paid Routing APIs?

Google charges for using routing-related APIs because their servers perform the path computation.

This project follows a different approach:

1. Use the Google Maps JavaScript API only to display the map.
2. Build your own graph representation.
3. Implement shortest-path algorithms locally.
4. Compute routes using Python instead of Google's routing services.
5. Display the computed route back on the map.

In simple words,

**Google provides the map.**

**Your own algorithm provides the route.**

Because the routing logic runs locally, no paid routing service is required.

To use the project, simply generate your own Google Maps JavaScript API key from Google Cloud Console and replace the placeholder API key inside the project.

---

# ✨ Features

* 🌍 Interactive Google Maps interface
* 📍 Source and destination selection
* ⚡ Dijkstra's Algorithm implementation
* 🚀 A* Search Algorithm implementation
* 🧠 Graph-based shortest path computation
* 🔄 Flask backend
* 📊 Interactive frontend
* 🎓 Educational implementation of graph algorithms
* 💡 Low-cost alternative for routing algorithm experimentation

---

# ⚠️ Current Limitation

Currently, the project map contains graph data only for **Ludhiana, Punjab**.

This limitation exists because generating and processing graph data for a very large geographical area requires significantly more memory and computational resources. The project was developed and tested on a low-end machine, so the graph was intentionally limited to ensure smooth local execution.

If someone has access to a more powerful computer, the project can be extended easily by:

* Adding graph data for additional cities
* Increasing the map coverage
* Expanding the graph database
* Modifying the graph generation code

The algorithms themselves are not limited to Ludhiana; only the current graph dataset is.

---

# 🏗️ Project Architecture

```
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

```
Route-Optimizer-Google-maps/

│── app.py
│── algorithms.py
│── graph.py
│── index.html
│── README.md
```

---

# 💻 Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript
* Google Maps JavaScript API

### Backend

* Python
* Flask

### Algorithms

* Dijkstra's Algorithm
* A* Search Algorithm

---

# ⚙️ Installation

Clone the repository.

```bash
git clone https://github.com/RhydamKumar/Route-Optimizer-Google-maps.git
```

Navigate into the project.

```bash
cd Route-Optimizer-Google-maps
```

Install Flask.

```bash
pip install flask
```

Start the application.

```bash
python app.py
```

Generate your own Google Maps JavaScript API key from Google Cloud Console and replace the placeholder API key inside the project.

Open the application in your browser.

---

# 🚀 Usage

1. Start the Flask server.
2. Open the application.
3. Enter the source location.
4. Enter the destination.
5. Run the selected algorithm.
6. View the optimized route displayed on Google Maps.

---

# 🧮 Algorithms Implemented

## Dijkstra's Algorithm

* Complete
* Optimal
* Suitable for weighted graphs
* Guarantees the shortest path

---

## A* Search Algorithm

* Heuristic-based search
* Faster for many practical cases
* Widely used in navigation systems
* Optimal when an admissible heuristic is used

---

# 🎯 Educational Objectives

This project demonstrates practical implementation of:

* Graph Theory
* Shortest Path Algorithms
* Flask Backend Development
* Google Maps Integration
* Frontend-Backend Communication
* Algorithm Visualization

---

# 🚀 Future Improvements

* Add support for multiple cities
* Automatic graph generation
* Compare execution time of algorithms
* Alternative route suggestions
* Traffic-aware routing
* Better UI/UX
* Cloud deployment
* Larger graph datasets

---

# 🤝 Contributing

Contributions are welcome.

Feel free to fork the repository, improve the project, and submit a Pull Request.

---

# 📜 License

This project is intended for educational and research purposes.

You are free to use, modify, and improve it while providing appropriate credit to the original repository.

---

# 👨‍💻 Author

**Rhydam Kumar**

GitHub:
https://github.com/RhydamKumar

---

⭐ If you found this project useful, please consider giving it a star.
