from collections import deque


class BFS:
    def __init__(self, graph, isDirectedGraph):
        """
        Breadth-first search implementation for unweighted graphs. Graph must be a map of each vertex to an iterable
        container of adjacent vertices.

        :param graph: graph in adjacency list format
        :param isDirectedGraph: whether the edges in the graph are directed (True) or undirected (False)
        """
        self.graph = graph
        self.isDirectedGraph = isDirectedGraph
        self.nVertices = len(graph)
        self.reset()

    def reset(self):
        self.distance = [float('inf')] * self.nVertices
        self.parent = [None] * self.nVertices
        # Processed array is necessary to avoid processing the same edge twice in undirected graphs.
        self.processed = [False] * self.nVertices
        self.discovered = [False] * self.nVertices

    def getPath(self, vertex):
        path = []
        while vertex:
            path.append(vertex)
            vertex = self.parent[vertex]
        return path[::-1]

    def onVertexBefore(self, u):
        pass

    def onVertexAfter(self, u):
        pass

    def onEdge(self, u, v):
        pass

    def onBeforeSearchAllPass(self, srcVertex):
        pass

    def searchVertex(self, srcVertex):
        u = srcVertex
        self.distance[srcVertex] = 0
        self.discovered[srcVertex] = True
        q = deque([srcVertex])

        while q:
            u = q.popleft()
            self.onVertexBefore(u)
            self.processed[u] = True
            for v in self.graph[u]:
                if self.isDirectedGraph or not self.processed[v]:
                    self.onEdge(u, v)
                if not self.discovered[v]:
                    self.discovered[v] = True
                    self.parent[v] = u
                    self.distance[v] = self.distance[u] + 1
                    q.append(v)
            self.onVertexAfter(u)

        return self

    def searchAllVertices(self):
        nVertices = len(self.graph)
        for vertex in range(len(self.graph)):
            if not self.discovered[vertex]:
                self.onBeforeSearchAllPass(vertex)
                self.searchVertex(vertex)
        return self
