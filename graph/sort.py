from collections import deque
from graph.dfs import DFS, EdgeType


class NotAcyclicGraphException(Exception):
    pass


class TopologicalSorter(DFS):
    def __init__(self, dag, checkForCycles=True):
        super().__init__(dag, isDirectedGraph=True)
        self.checkForCycles = checkForCycles
        self.sortedVertices = deque()

    def onEdge(self, u, v):
        if self.checkForCycles and self.getEdgeType(u, v) == EdgeType.BACK:
            raise NotAcyclicGraphException

    def onVertexAfter(self, u):
        self.sortedVertices.appendleft(u)


def topologicalSort(dag, checkForCycles=True):
    tps = TopologicalSorter(dag, checkForCycles)
    tps.searchAllVertices()
    return tps.sortedVertices

