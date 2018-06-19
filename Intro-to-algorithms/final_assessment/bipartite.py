#
# Write a function, `bipartite` that
# takes as input a graph, `G` and tries
# to divide G into two sets where
# there are no edges between elements of the
# the same set - only between elements in
# different sets.
# If two sets exists, return one of them
# or `None` otherwise
# Assume G is connected
#


def bipartite(G):
    first_node = G.keys()[0]
    results = {first_node: 1}
    nodes = [first_node]
    while nodes:
        node = nodes.pop(0)
        # label of neighbours should be different
        neighbour_label = abs(1-results[node])
        for neighbour in G[node]:
            if neighbour in results:
                # already signed another label
                if neighbour_label != results[neighbour]:
                    return None
            else:
                results[neighbour] = neighbour_label
                nodes.append(neighbour)
    return {node for node, label in results.items() if label == 1}


########
#
# Test

def make_link(G, node1, node2, weight=1):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = weight
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = weight
    return G


def test():
    edges = [(1, 2), (2, 3), (1, 4), (2, 5),
             (3, 8), (5, 6)]
    G = {}
    for n1, n2 in edges:
        make_link(G, n1, n2)
    g1 = bipartite(G)
    assert (g1 == set([1, 3, 5]) or
            g1 == set([2, 4, 6, 8]))
    edges = [(1, 2), (1, 3), (2, 3)]
    G = {}
    for n1, n2 in edges:
        make_link(G, n1, n2)
    g1 = bipartite(G)
    assert g1 == None


if __name__ == '__main__':
    print test()
