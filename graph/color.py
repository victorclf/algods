from .bfs import BFS


class _NotTwoColorableException(Exception):
    pass


class _IsTwoColorableBFS(BFS):
    def __init__(self, graph, isDirectedGraph):
        super().__init__(graph, isDirectedGraph)
        self.color = [None] * self.nVertices  # None, 0 or 1

    def onEdge(self, u, v):
        if self.color[u] == self.color[v]:
            raise _NotTwoColorableException
        self.color[v] = self.color[u] ^ 1  # assign opposite color

    def onBeforeSearchAllPass(self, srcVertex):
        self.color[srcVertex] = 0


def isTwoColorable(graph, isDirectedGraph):
    bfs = _IsTwoColorableBFS(graph, isDirectedGraph)
    try:
        bfs.searchAllVertices()
    except _NotTwoColorableException:
        return False
    return True
