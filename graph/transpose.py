def transpose(unweightedDirectedGraph):
    g = unweightedDirectedGraph
    newGraph = [[] for _ in range(len(g))]
    for u in range(len(g)):
        for v in g[u]:
            newGraph[v].append(u)
    return newGraph


if __name__ == '__main__':
    g = [[1],
         [2],
         [1]]
    gT = [[],
         [0, 2],
         [1]]

    assert transpose(g) == gT
