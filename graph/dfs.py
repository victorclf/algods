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
        nVertices = len(self.graph)
        for vertex in range(len(self.graph)):
            if not self.discovered[vertex]:
                self.searchVertex(vertex)


class _FoundCycleException(Exception):
    pass


class _FindCycleDFS(DFS):
    def onEdge(self, u, v):
        if self.getEdgeType(u, v) == EdgeType.BACK:
            raise _FoundCycleException(self.getPath(u) + [v])


def isCyclicGraph(graph, isDirectedGraph):
    try:
        _FindCycleDFS(graph, isDirectedGraph).searchAllVertices()
    except _FoundCycleException:
        return True
    return False


if __name__ == '__main__':
    directedGraph = [[1, 3],  # u = 0
                     [4],  # v = 1
                     [4, 5],  # w = 2
                     [1],  # x = 3
                     [3],  # y = 4
                     [5]]  # z = 5
    dfsDg1 = DFS(directedGraph, isDirectedGraph=True)
    dfsDg1.searchAllVertices()
    assert dfsDg1.parent == [None, 0, None, 4, 1, 2]
    assert all(dfsDg1.discovered)
    assert all(dfsDg1.processed)
    assert dfsDg1.entryTime == [1, 2, 9, 4, 3, 10]
    assert dfsDg1.exitTime == [8, 7, 12, 5, 6, 11]

    acyclicGraph = [[1],
                    [2],
                    []]
    cyclicGraph = [[1],
                    [2],
                    [0]]
    assert not isCyclicGraph(acyclicGraph, isDirectedGraph=False)
    assert isCyclicGraph(cyclicGraph, isDirectedGraph=False)
    assert isCyclicGraph(directedGraph, isDirectedGraph=True)

