from graph.bfs import BFS
from graph.dfs import DFS, EdgeType
from graph.transpose import transpose
from graph.sort import topologicalSort


class _StronglyConnectedComponentFinder(DFS):
    def onVertexAfter(self, u):
        self.components[-1].append(u)

    def onBeforeSearchAllPass(self, srcVertex):
        self.components.append([])

    def searchAllVertices(self):
        if not hasattr(self, 'sortedVertices'):
            self.components = []
            self.sortedVertices = topologicalSort(self.graph, checkForCycles=False)
            self.graph = transpose(self.graph)

        for vertex in self.sortedVertices:
            if not self.discovered[vertex]:
                self.onBeforeSearchAllPass(vertex)
                self.searchVertex(vertex)


def findStronglyConnectedComponents(directedGraph):
    """
    Uses Kosaraju's algorithm whose simplicity is offset by its need of two DFS passes unlike other
    more efficient algorithms which require a single one.
    """
    sccFinder = _StronglyConnectedComponentFinder(directedGraph, isDirectedGraph=True)
    sccFinder.searchAllVertices()
    return sccFinder.components


class _ConnectedComponentBFS(BFS):
    def __init__(self, graph, isDirectedGraph):
        super().__init__(graph, isDirectedGraph)
        self.components = []

    def onVertexAfter(self, u):
        self.components[-1].append(u)

    def onBeforeSearchAllPass(self, srcVertex):
        self.components.append([])


def findConnectedComponents(graph, isDirectedGraph):
    cc = _ConnectedComponentBFS(graph, isDirectedGraph)
    cc.searchAllVertices()
    return cc.components
