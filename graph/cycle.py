from graph.dfs import DFS, EdgeType


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

