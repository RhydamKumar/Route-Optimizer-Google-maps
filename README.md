# 🚗 Route Optimizer using Google Maps (Visualization) & Local Pathfinding Algorithms

![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow)
![HTML](https://img.shields.io/badge/HTML-5-orange)
![CSS](https://img.shields.io/badge/CSS-3-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

A lightweight, research-oriented route optimization platform that enables **developers**, **students**, and **researchers** to test and visualize shortest-path algorithms **without relying on paid routing APIs**.

Unlike commercial navigation systems, this project uses **Google Maps only for visualization**, while all route calculations are performed locally using custom implementations of **Dijkstra's Algorithm** and **A\* Search Algorithm**.

---

# 📖 Overview

**Route Optimizer** is an educational and research-focused project that demonstrates how shortest-path algorithms can be implemented independently of commercial routing services.

Most navigation applications rely on cloud-based routing APIs to compute the shortest path. While these APIs are highly accurate, they become expensive when developers need to perform thousands of routing requests during testing or research.

This project solves that problem by:

- Using Google Maps only as the map interface.
- Computing all routes locally.
- Allowing complete control over routing algorithms.
- Providing a free environment for experimentation.

The project is ideal for:

- 🎓 College Projects
- 🔬 Academic Research
- 💻 Algorithm Development
- 📚 Learning Graph Theory
- 🚗 Route Optimization Experiments

---

# 🤔 Why Use This Project When Google Maps Already Exists?

This is the most common question about the project.

## Google Maps is Excellent—but It Isn't Always Practical

Google Maps provides one of the world's best navigation services.

However, if you're building your own navigation application, researching shortest-path algorithms, or developing academic projects, you'll often need thousands of routing requests.

Google Maps Platform uses a **usage-based pricing model** for routing APIs. While suitable for production applications, repeated routing requests during testing and experimentation can become expensive for:

- Students
- Researchers
- Hobby developers
- Startups
- Educational institutions

Our goal is **not to replace Google Maps**.

Instead, this project provides a **free and customizable research environment** where routing algorithms can be implemented, tested, compared, and improved without depending on paid routing services.

---

# 💡 Our Approach

Instead of asking Google Maps to calculate routes:

✅ Google Maps is used **only as the map background**.

✅ The routing engine is implemented entirely inside this project.

The shortest path is calculated locally using custom implementations of:

- Dijkstra's Algorithm
- A* (A-Star) Search Algorithm

This means:

- No routing API requests
- No routing API charges
- Complete control over the algorithms
- Easy experimentation
- Better understanding of graph algorithms

---

# ✨ Why This Project is Useful

### 💰 Cost Effective

No paid routing APIs are required for shortest-path computation.

---

### 🧑‍🎓 Student Friendly

Perfect for:

- College projects
- University assignments
- Final-year projects

Students can study and modify routing algorithms without worrying about API costs.

---

### 🔬 Research Friendly

Researchers often compare multiple algorithms.

This project allows:

- Algorithm benchmarking
- Performance comparison
- Graph experimentation
- Heuristic testing

without consuming paid API requests.

---

### 💻 Runs Locally

Everything runs on your own computer.

Benefits include:

- Faster experimentation
- No dependency on cloud routing
- Easy debugging

---

### 🔒 Privacy

Since route computation happens locally:

- No routing data is sent to external servers.
- Experimental datasets remain on your machine.

---

### 🌐 Offline Capability

Once the required map data has been loaded, route calculations continue to work locally without requiring additional routing API calls.

---

# ⚙️ How It Works

1. Google Maps displays the map.
2. The road network is converted into a graph.
3. Nodes represent road intersections.
4. Edges represent roads.
5. The user selects source and destination.
6. The chosen algorithm computes the shortest path.
7. The resulting path is drawn on the map.

Unlike commercial navigation services,

> **Google Maps never computes the route.**

The optimization happens entirely inside the application.

---

# 📍 Current Scope

The current implementation focuses only on the **Ludhiana road network**.

## Why Only Ludhiana?

A complete road graph for an entire country contains millions of nodes and edges.

Supporting such a large dataset would significantly increase:

- Memory usage
- Storage requirements
- Loading time
- Graph preprocessing time

Since the goal of this project is educational and research-oriented, the dataset has intentionally been limited to **Ludhiana**.

This keeps the project:

- ⚡ Fast
- 📦 Lightweight
- 💻 Easy to run
- 🎓 Suitable for students
- 🔬 Suitable for research

---

## Future Expansion

The routing engine is completely independent of the map itself.

By replacing the graph dataset, this application can support:

- Additional cities
- Entire states
- Larger regions
- Country-wide routing

without changing the core algorithms.

### Current Coverage

📍 **Ludhiana, Punjab, India**

Future versions may include support for multiple cities through optimized graph-loading techniques.

---

# ✨ Features

- 🗺️ Google Maps Integration (Visualization Only)
- 🚗 Local Route Optimization
- 📍 Interactive Map
- ⚡ Dijkstra's Algorithm
- ⭐ A* Search Algorithm
- 📏 Distance Calculation
- 📍 Route Visualization
- 💻 Local Processing
- 🔒 Privacy-Friendly Architecture
- 🌐 Offline Routing after Initial Data Loading
- 📱 Responsive User Interface
- 🧠 Modular Algorithm Implementation
- 🛠️ Easy to Extend with New Algorithms

---

# 🛠️ Tech Stack

## Frontend

- HTML5
- CSS3
- JavaScript (ES6)

## Algorithms

- Dijkstra's Algorithm
- A* Search Algorithm

## Visualization

- Google Maps JavaScript API

> **Note:** Google Maps is used only for displaying the map. Route optimization is performed entirely by the algorithms implemented in this project.

---

# 📂 Project Structure

```text
Route-Optimizer/
│
├── index.html
├── css/
│   └── style.css
│
├── js/
│   ├── script.js
│   ├── graph.js
│   ├── dijkstra.js
│   ├── astar.js
│   └── ...
│
├── assets/
├── images/
├── README.md
└── ...
```

*(The folder structure may vary depending on future updates.)*

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/RhydamKumar/Route-Optimizer-Google-Maps.git
```

## Open Project

```bash
cd Route-Optimizer-Google-Maps
```

## Add Google Maps API Key

Replace the API key inside:

```html
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places"></script>
```

> **Important:** The API key is required only for rendering the map interface.
>
> **No routing requests are sent to Google Maps.**

## Run

Open

```
index.html
```

or launch the project using **Live Server** in Visual Studio Code.
---

# 🧠 Algorithms Used

This project currently implements two of the most widely used shortest-path algorithms in graph theory.

## 1. Dijkstra's Algorithm

Dijkstra's Algorithm computes the shortest path between two nodes in a weighted graph with **non-negative edge weights**.

### Characteristics

- Guarantees the shortest path
- Explores nodes based on the minimum accumulated distance
- Reliable and widely used in networking and GIS applications

### Advantages

- ✅ Always finds the optimal path
- ✅ Simple and easy to understand
- ✅ Works well on weighted graphs

### Limitations

- Slightly slower than heuristic-based algorithms on very large graphs.

---

## 2. A* (A-Star) Search Algorithm

A* Search improves upon Dijkstra's Algorithm by using a heuristic function to estimate the remaining distance to the destination.

Instead of exploring every possible node, A* prioritizes nodes that are more likely to lead toward the goal.

### Characteristics

- Combines path cost with heuristic estimation
- Usually explores fewer nodes
- Faster in many practical scenarios

### Advantages

- ✅ Faster than Dijkstra in many cases
- ✅ Efficient on large graphs
- ✅ Produces the shortest path when using an admissible heuristic

---

# 📊 Algorithm Comparison

| Feature | Dijkstra | A* Search |
|----------|-----------|------------|
| Guarantees Shortest Path | ✅ | ✅ |
| Uses Heuristic | ❌ | ✅ |
| Speed | Moderate | Fast |
| Nodes Explored | More | Fewer |
| Suitable for Large Graphs | Good | Excellent |
| Easy to Understand | ✅ | ✅ |

---

# ⚡ Time Complexity

| Algorithm | Time Complexity |
|------------|-----------------|
| Dijkstra | O((V + E) log V) |
| A* Search | Depends on heuristic (typically faster in practice) |

Where:

- **V** = Number of vertices (road intersections)
- **E** = Number of edges (roads)

---

# 📈 Performance

Since route calculations are performed locally:

- No network latency during routing
- Faster experimentation
- Easy algorithm benchmarking
- Real-time comparison between routing algorithms
- Suitable for educational demonstrations

---

# 📚 Applications

This project can be used for:

- 🎓 Academic Projects
- 🔬 Research on Graph Algorithms
- 🚚 Delivery Route Optimization
- 🏙️ Smart City Research
- 🚗 Navigation System Prototyping
- 📊 Algorithm Performance Analysis
- 🧠 AI Pathfinding Experiments
- 🗺️ GIS Learning
- 📖 Graph Theory Education

---

# 🔮 Future Improvements

The project has been designed to be easily extensible.

Planned improvements include:

- 🌍 Support for Multiple Cities
- 🛣️ Automatic Road Graph Generation
- 🚦 Traffic-Aware Route Planning
- 🚗 Multiple Vehicle Support
- 📍 Multi-Destination Optimization
- 📈 Performance Dashboard
- 📊 Algorithm Benchmarking
- 🧠 Additional Algorithms:
  - Bellman-Ford
  - Floyd-Warshall
  - Bidirectional Search
  - Bidirectional A*
  - Breadth-First Search (BFS)
  - Depth-First Search (DFS)
- 📁 Route Export
- 💾 Save Favorite Routes
- 📱 Progressive Web App (PWA) Support
- ☁️ Cloud Synchronization
- 🌙 Dark Mode

---

# 🤝 Contributing

Contributions are always welcome!

If you'd like to improve the project:

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push the branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

Please ensure your code is properly documented and tested before submitting.

---

# 🧪 Testing

You can test the application by:

- Selecting different source and destination points
- Comparing Dijkstra and A* results
- Measuring execution time
- Observing the generated shortest path
- Modifying the graph to test custom scenarios

---

# 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project for educational and research purposes.

---

# 👨‍💻 Author

## Rhydam Kumar

Passionate about:

- Data Structures & Algorithms
- Web Development
- Artificial Intelligence
- Software Engineering

If you found this project helpful, consider giving it a ⭐ on GitHub!

---

# 🙏 Acknowledgements

Special thanks to:

- The open-source community
- Google Maps Platform for map visualization
- Contributors to graph theory and shortest-path algorithm research
- Everyone who supports open-source educational projects

---

# 📢 Disclaimer

This project is intended for **educational, research, and experimental purposes only**.

Key points:

- Google Maps is used **only as the visualization layer**.
- All shortest-path calculations are implemented independently within this project.
- No Google routing or optimization APIs are used for path computation.
- The current implementation is intentionally limited to the **Ludhiana, Punjab** road network to keep the graph lightweight and suitable for algorithm experimentation.
- The architecture is designed to support additional cities and larger datasets in future versions.

This project is **not intended to replace commercial navigation systems**, but to provide an accessible platform for learning, testing, and researching pathfinding algorithms.

---

# ⭐ Support

If you found this project useful:

- ⭐ Star the repository
- 🍴 Fork the project
- 🛠️ Contribute improvements
- 📝 Report issues
- 💡 Suggest new features

Your support helps improve the project and encourages further development.

---

> **"Understanding algorithms is easier when you can see them in action."**
>
> **Route Optimizer** provides a practical environment for learning, experimenting, and comparing shortest-path algorithms without the limitations of paid routing services.
