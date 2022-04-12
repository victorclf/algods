from enum import Enum, auto


class EdgeType(Enum):
    TREE = auto()
    BACK = auto()
    FORWARD = auto()
    CROSS = auto()


class DFS:
    def __init__(self, graph, isDirectedGraph):
        self.graph = graph
        self.isDirectedGraph = isDirectedGraph
        self.nVertices = len(graph)
        self.parent = [None] * self.nVertices
        # Processed array is necessary to avoid processing the same edge twice in undirected graphs.
        self.processed = [False] * self.nVertices
        self.discovered = [False] * self.nVertices
        self.entryTime = [None] * self.nVertices
        self.exitTime = [None] * self.nVertices
        self.time = 0

    def getPath(self, vertex):
        path = []
        while vertex:
            path.append(vertex)
            vertex = self.parent[vertex]
        return path[::-1]

    def getEdgeType(self, u, v):
        if self.parent[v] == u:
            return EdgeType.TREE

        if self.discovered[v] and not self.processed[v]:
            return EdgeType.BACK

        if self.processed[v] and self.entryTime[v] > self.entryTime[u]:
            return EdgeType.FORWARD

        if self.processed[v] and self.entryTime[v] < self.entryTime[u]:
            return EdgeType.CROSS

        raise Exception

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
        self.onVertexBefore(u)
        self.discovered[u] = True
        self.time += 1
        self.entryTime[u] = self.time
        for v in self.graph[u]:
            if not self.discovered[v]:
                self.parent[v] = u
                self.onEdge(u, v)
                self.searchVertex(v)
            elif self.isDirectedGraph or (not self.processed[v] and not self.parent[v] == u):
                self.onEdge(u, v)
        self.onVertexAfter(u)
        self.time += 1
        self.exitTime[u] = self.time
        self.processed[u] = True

    def searchAllVertices(self):
        for vertex in range(len(self.graph)):
            if not self.discovered[vertex]:
                self.onBeforeSearchAllPass(vertex)
                self.searchVertex(vertex)
