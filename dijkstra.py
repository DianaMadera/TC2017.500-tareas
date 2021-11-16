from queue import PriorityQueue


class Graph:
    #Constructor
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    #Function to add an edge
    def addEdge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

    #Dijkstra's algorithm
    def dijkstra(self, start_vertex):
        D = {v:float('inf') for v in range(self.v)}
        D[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.append(current_vertex)

            for neighbor in range(self.v):
                if self.edges[current_vertex][neighbor] != -1:
                    distance = self.edges[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        return D

# Driver code
g = Graph(28)
g.addEdge(0, 1, 5)
g.addEdge(0, 6, 3)
g.addEdge(1, 0, 5)
g.addEdge(1, 2, 1)
g.addEdge(1, 4, 1)
g.addEdge(2, 1, 1)
g.addEdge(2, 3, 1)
g.addEdge(2, 4, 1)
g.addEdge(3, 2, 1)
g.addEdge(3, 5, 2)
g.addEdge(4, 1, 1)
g.addEdge(4, 2, 1)
g.addEdge(4, 5, 2)
g.addEdge(4, 7, 1)
g.addEdge(5, 3, 2)
g.addEdge(5, 4, 2)
g.addEdge(5, 9, 2)
g.addEdge(5, 12, 1)
g.addEdge(6, 0, 3)
g.addEdge(6, 10, 6)
g.addEdge(6, 18, 4)
g.addEdge(7, 4, 1)
g.addEdge(7, 8, 0)
g.addEdge(7, 10, 0)
g.addEdge(8, 7, 0)
g.addEdge(8, 11, 0)
g.addEdge(8, 12, 2)
g.addEdge(9, 5, 2)
g.addEdge(9, 17, 2)
g.addEdge(9, 22, 2)
g.addEdge(10, 6, 6)
g.addEdge(10, 7, 0)
g.addEdge(10, 11, 0)
g.addEdge(10, 13, 1)
g.addEdge(11, 8, 0)
g.addEdge(11, 10, 0)
g.addEdge(11, 14, 1)
g.addEdge(11, 15, 2)
g.addEdge(12, 5, 1)
g.addEdge(12, 8, 2)
g.addEdge(12, 16, 0)
g.addEdge(12, 17, 0)
g.addEdge(13, 10, 1)
g.addEdge(13, 14, 0)
g.addEdge(13, 18, 5)
g.addEdge(13, 19, 2)
g.addEdge(14, 11, 1)
g.addEdge(14, 13, 0)
g.addEdge(14, 15, 1)
g.addEdge(14, 20, 2)
g.addEdge(15, 11, 2)
g.addEdge(15, 14, 1)
g.addEdge(15, 16, 0)
g.addEdge(15, 20, 1)
g.addEdge(16, 12, 0)
g.addEdge(16, 15, 0)
g.addEdge(16, 17, 0)
g.addEdge(16, 21, 1)
g.addEdge(17, 9, 2)
g.addEdge(17, 12, 0)
g.addEdge(17, 16, 0)
g.addEdge(17, 22, 5)
g.addEdge(18, 6, 4)
g.addEdge(18, 13, 5)
g.addEdge(18, 19, 2)
g.addEdge(18, 23, 2)
g.addEdge(19, 13, 2)
g.addEdge(19, 18, 2)
g.addEdge(19, 20, 1)
g.addEdge(19, 24, 3)
g.addEdge(20, 14, 2)
g.addEdge(20, 15, 1)
g.addEdge(20, 19, 1)
g.addEdge(20, 21, 0)
g.addEdge(20, 25, 1)
g.addEdge(20, 26, 5)
g.addEdge(21, 16, 1)
g.addEdge(21, 20, 0)
g.addEdge(21, 22, 4)
g.addEdge(21, 25, 0)
g.addEdge(22, 9, 2)
g.addEdge(22, 17, 5)
g.addEdge(22, 21, 4)
g.addEdge(23, 18, 2)
g.addEdge(24, 19, 3)
g.addEdge(25, 20, 1)
g.addEdge(25, 21, 0)
g.addEdge(25, 27, 5)
g.addEdge(26, 20, 5)
g.addEdge(27, 25, 5)

D = g.dijkstra(0)

for vertex in range(len(D)):
    print("Distance from vertex 0 to vertex", vertex, "is", D[vertex])

    

