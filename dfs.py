class Graph:
    #function to fill the array with zeros given n size
    def __init__(self,n):
        self.n=n
        self.aMatrix= [[0 for i in range(n)] for i in range(n)]
        self.visited= [[False for i in range(n)] for i in range(n)]
    
    #function to indicate connection between nodes
    def addEdge(self,i,j):
        self.aMatrix[i][j]=1
    
    def printMatrix(self):
        for i in range(self.n):
            print()
            for j in range (self.n):
                    print(self.aMatrix[i][j], end=" ")

    #DFS algorithm implementation
    def DFS(self):
        stack = []
        visited = [ 0 for i in range(self.n) ]
        stack.append(0)
        while len(stack) > 0:
            current = stack.pop()
            if visited[current] == 0:
                visited[current] = 1
                print(current, end=" ")
                for j in reversed(range(self.n)):
                    if self.aMatrix[current][j] == 1 and visited[j] == 0:
                        stack.append(j)

#code test
g=Graph(4)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

g.DFS()
