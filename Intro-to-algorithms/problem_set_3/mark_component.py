# Rewrite `mark_component` to not use recursion
# and instead use the `open_list` data structure
# discussed in lecture
#


def mark_component(G, node, marked):
    open_list = [node]
    while open_list:
        current_node = open_list.pop()
        marked[current_node] = True
        for neighbor in G[current_node]:
            if neighbor not in marked:
                open_list.append(neighbor)
    return len(marked)


def mark_component_new(G, node, marked):

    open_list = [node]
    while len(open_list) > 0:
        current_node = open_list[0]
        del open_list[0]
        marked[current_node] = True
        for neighbor in G[current_node]:
            if neighbor not in marked:
                open_list.append(neighbor)
    return len(marked)


def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G


def test():
    test_edges = [(1, 2), (2, 3), (4, 5), (5, 6)]
    G = {}
    for n1, n2 in test_edges:
        make_link(G, n1, n2)
    marked = {}
    assert mark_component_new(G, 1, marked) == 3
    assert 1 in marked
    assert 2 in marked
    assert 3 in marked
    assert 4 not in marked
    assert 5 not in marked
    assert 6 not in marked


if __name__ == '__main__':
    test()