from collections import deque


def bfs(graph, srcVertex, isDirectedGraph=False, discovered=None, onVertexBefore=lambda u: None, onVertexAfter=lambda u: None, onEdge=lambda u, v: None):
    """
    Breadth-first search implementation for unweighted graphs. Graph must be a map of each vertex to an iterable
    container of adjacent vertices.

    :param graph: graph in adjacency list format
    :param srcVertex: id of the source vertex
    :param isDirectedGraph: whether the edges in the graph are directed (True) or undirected (False)
    :param discovered: list of bool indicating which vertices have already been found. Used for tracking the vertices
                        throughout multiple calls to bfs.
    :param onVertexBefore: callback before processing vertex u
    :param onVertexAfter: callback after processing vertex u
    :param onEdge: callback when processing edge u, v
    :return: a tuple with maps: distance, parent, discovered, i.e. number of edges to reach each vertex from srcVertex,
             the parent of each vertex in a path from srcVertex to vertex, the vertices which have been found traversing
             from srcVertex
    """
    nVertices = len(graph)
    distance = [float('inf')] * nVertices
    parent = [None] * nVertices
    # Processed array is necessary to avoid processing the same edge twice in undirected graphs.
    processed = [False] * nVertices if discovered is None else discovered.copy()
    discovered = [False] * nVertices if discovered is None else discovered

    distance[srcVertex] = 0
    discovered[srcVertex] = True
    q = deque([srcVertex])

    while q:
        u = q.popleft()
        onVertexBefore(u)
        processed[u] = True
        for v in graph[u]:
            if isDirectedGraph or not processed[v]:
                onEdge(u, v)
            if not discovered[v]:
                discovered[v] = True
                parent[v] = u
                distance[v] = distance[u] + 1
                q.append(v)
        onVertexAfter(u)

    return distance, parent, discovered


def countConnectedComponents(graph):
    nVertices = len(graph)
    discovered = None
    components = 0
    for vertex in range(len(graph)):
        if not discovered or not discovered[vertex]:
            components += 1
            distance, parent, discovered = bfs(graph, vertex, discovered=discovered)
    return components


class _NotTwoColorableException(Exception):
    pass


def isTwoColorable(graph):
    def onEdge(u, v):
        if color[u] == color[v]:
            raise _NotTwoColorableException
        color[v] = color[u] ^ 1  # assign opposite color

    nVertices = len(graph)
    discovered = None
    color = [None] * nVertices  # None, 0 or 1
    for vertex in range(len(graph)):
        if not discovered or not discovered[vertex]:
            color[vertex] = 0
            try:
                distance, parent, discovered = bfs(graph, vertex, discovered=discovered, onEdge=onEdge)
            except _NotTwoColorableException:
                return False
    return True


def _isUndirectedGraph(graph):
    edges = set()
    for u in range(len(graph)):
        for v in graph[u]:
            edges.add((u, v))

    for u, v in edges:
        if (v, u) not in edges:
            return False
    return True


if __name__ == '__main__':
    undirectedGraph = [[1, 4],  # r = 0
                       [0, 5],  # s = 1
                       [3, 5, 6],  # t = 2
                       [2, 6, 7],  # u = 3
                       [0],  # v = 4
                       [1, 2, 6],  # w = 5
                       [2, 3, 5, 7],  # x = 6
                       [3, 6]]  # y = 7
    threeComponentGraph = [[1],
                            [0],
                            [3],
                            [2],
                            [5],
                            [4, 6],
                            [5]]
    twoColorableGraph = [[3, 4],
                         [4],
                         [4],
                         [0],
                         [0, 1, 2]]

    assert _isUndirectedGraph(undirectedGraph)
    assert _isUndirectedGraph(threeComponentGraph)
    assert _isUndirectedGraph(twoColorableGraph)

    distance, parent, discovered = bfs(undirectedGraph, 1)
    assert distance == [1, 0, 2, 3, 2, 1, 2, 3]
    assert parent == [1, None, 5, 2, 0, 1, 5, 6]
    assert all(discovered)

    assert countConnectedComponents(undirectedGraph) == 1
    assert countConnectedComponents(threeComponentGraph) == 3

    assert not isTwoColorable(undirectedGraph)
    assert isTwoColorable(twoColorableGraph)