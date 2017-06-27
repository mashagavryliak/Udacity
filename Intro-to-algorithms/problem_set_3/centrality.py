#
# Write centrality_max to return the maximum distance
# from a node to all the other nodes it can reach
#


def centrality_max(G, v):
    distances = {v: 0}
    open_list = [v]
    while open_list:
        current_node = open_list.pop()
        for neighbor in G[current_node]:
            if neighbor not in distances:
                distances[neighbor] = distances[current_node] + 1
                open_list.append(neighbor)
    return max(distances.values())


def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G


def test():
    chain = ((1,2), (2,3), (3,4), (4,5), (5,6))
    G = {}
    for n1, n2 in chain:
        make_link(G, n1, n2)
    assert centrality_max(G, 1) == 5
    assert centrality_max(G, 3) == 3
    tree = ((1, 2), (1, 3),
            (2, 4), (2, 5),
            (3, 6), (3, 7),
            (4, 8), (4, 9),
            (6, 10), (6, 11))
    G = {}
    for n1, n2 in tree:
        make_link(G, n1, n2)
    assert centrality_max(G, 1) == 3
    assert centrality_max(G, 11) == 6


if __name__ == '__main__':
    test()