## Section 1: Problem Selection

**Problem Statement:** The chosen real-world problem involves optimising driving routes between two points, focusing on the specific need of finding the quickest path from University College Dublin (UCD) to Westmeath during rush hour traffic. This focuses on the journey from UCD to the Dundrum M50 exit. The motivation stems from personal experience where conventional navigation systems like Google Maps do not always provide the quickest route, particularly during peak traffic hours. The proposed system will seek to incorporate less traditional routes, such as through local housing areas, where navigation systems typically do not direct traffic, potentially reducing travel time significantly.

**Relevance and Significance:** This problem is highly relevant for daily commuters and individuals who must travel frequently for activities like sports or family commitments. The current solutions often fail to adapt quickly to real-time traffic conditions or consider unconventional routes that could save time. By improving the accuracy and efficiency of route recommendations, the system can significantly impact daily commuting, reduce travel time, and enhance the overall driving experience.

## Section 2: System Design Proposal

**Functionalities:**
- **Dynamic Route Calculation:** The system will calculate the quickest route from a starting point (UCD) to a sub-destination (Dundrum M50 exit) considering current traffic conditions and unconventional paths like local housing areas.
- **Real-Time Traffic Integration:** Incorporate real-time traffic data to update and adapt routes as conditions change.

**Input/Output Requirements:**
- **Input:** Starting future time
- **Output:** Optimal route with estimated travel time and distance.

**Key Operations:**
- **Graph Construction:** Build and update a graph where nodes represent intersections and edges represent roads, with weights reflecting travel time which could change dynamically based on traffic data.
- **Pathfinding Algorithm:** Implement an algorithm to find the shortest path in the graph considering the dynamic weights.
- **Data Update Mechanism:** Regular updates to the graph’s weights based on incoming traffic information to reflect current road conditions.

**Constraints:**
- **Accuracy:** The system must provide routes that are reliably quicker or comparable to existing navigation systems.
- **Performance:** Route calculation should be fast enough to be practical for real-time usage, providing updates as conditions change.
- **Scalability:** While initially focused on the route between UCD and Dundrum M50 exit, the system should be scalable to incorporate the full journey, and other routes and regions as needed.

## Section 3: Algorithm and Data Structure Selection

**Data Structure: Graph**
- **Justification:** A graph is an ideal data structure for modelling road networks where intersections and endpoints are represented as nodes, and the roads connecting them are edges with weights corresponding to travel times. Using a graph allows the application of efficient pathfinding algorithms to determine the quickest routes.

**Algorithm considerations:**
- **Dijkstra’s Algorithm:** This algorithm will be used for finding the shortest path from a single source to a single destination. It is suitable because it can handle graphs with non-negative weights, which correspond to the travel times on roads.
- **A* Algorithm (if applicable):** For enhanced performance, the A* algorithm may be considered. This algorithm uses heuristics to speed up the pathfinding process by estimating distances to the destination, which can be particularly useful in large road networks.

**Justification:** Dijkstra’s algorithm is renowned for its effectiveness and simplicity in finding the shortest path in weighted graphs. It is computationally efficient for our use case, where real-time response is critical. The A* algorithm provides a potentially faster solution by prioritising paths that are seemingly closer to the destination, thus reducing the overall computation time.

**Efficiency and Scalability:** Both algorithms are efficient for real-time applications, with Dijkstra’s algorithm working well for smaller to moderately sized graphs, and A* offering benefits in larger graphs with its heuristic approach.

**Complexity:** The complexity of Dijkstra’s algorithm is \(O((V + E) \log V)\) using a priority queue, where \(V\) is the number of vertices and \(E\) is the number of edges, suitable for real-time applications. A* has a similar complexity but can perform better in practice with the right heuristic.

**Trade-offs:**
- **Dijkstra’s vs. A*:** Dijkstra’s algorithm is straightforward and does not require an additional heuristic function, making it easier to implement and understand. However, A* can provide faster route calculations at the cost of developing and tuning a heuristic that accurately estimates distances.

## Section 4: Modelling and Implementation

**Modelling the Problem:**
- **Graph Construction:** The road network will be modelled as a graph where intersections are nodes and roads are edges. Traffic conditions affect the weights of the edges, which represent the dynamic travel times.
- **Dynamic Edge Weights:** Traffic data will be used to adjust the weights of the edges in real time, simulating current road conditions and providing up-to-date route recommendations.

**Implementation Considerations:**
- **Real-Time Data Handling:** A significant challenge will be integrating and processing real-time traffic data to continuously update edge weights. Efficient data handling strategies and fast update mechanisms are crucial.
- **Algorithm Implementation:** Implementing Dijkstra’s requires careful consideration of data structures for storing the graph and managing the priority queue to ensure efficient computation.

**Sample Data and Algorithm Use:**
- **Example:** If a user enters UCD as the start point and Westmeath as the destination during peak hours, the system will use the graph to compute the quickest path considering current traffic data, potentially suggesting a route through less congested residential areas which are dynamically calculated based on current conditions.
