# Decision problems are often just as hard as actually returning an answer.
# Show how a k-clique can be found using a solution to the k-clique decision
# problem.  Write a Python function that takes a graph G and a number k
# as input, and returns a list of k nodes from G that are all connected
# in the graph.  Your function should make use of "k_clique_decision(G, k)",
# which takes a graph G and a number k and answers whether G contains a k-clique.
# We will also provide the standard routines for adding and removing edges from a graph.

# Returns a list of all the subsets of a list of size k
def k_subsets(lst, k):
    if len(lst) < k:
        return []
    if len(lst) == k:
        return [lst]
    if k == 1:
        return [[i] for i in lst]
    return k_subsets(lst[1:], k) + map(lambda x: x + [lst[0]], k_subsets(lst[1:], k - 1))


# Checks if the given list of nodes forms a clique in the given graph.
def is_clique(G, nodes):
    for pair in k_subsets(nodes, 2):
        if pair[1] not in G[pair[0]]:
            return False
    return True


# Determines if there is clique of size k or greater in the given graph.
def k_clique_decision(G, k):
    nodes = G.keys()
    for i in range(k, len(nodes) + 1):
        for subset in k_subsets(nodes, i):
            if is_clique(G, subset):
                return True
    return False


def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G


def break_link(G, node1, node2):
    if node1 not in G:
        print "error: breaking link in a non-existent node"
        return
    if node2 not in G:
        print "error: breaking link in a non-existent node"
        return
    if node2 not in G[node1]:
        print "error: breaking non-existent link"
        return
    if node1 not in G[node2]:
        print "error: breaking non-existent link"
        return
    del G[node1][node2]
    del G[node2][node1]
    return {k: v for k, v in G.items() if v}


def k_clique(G, k):
    if not k_clique_decision(G, k):
        return False
    all_nodes = G.keys()
    if len(all_nodes) == k:
        return all_nodes

    while all_nodes:
        node1 = all_nodes.pop()
        neighbours = G[node1].keys()
        for node2 in neighbours:
            G = break_link(G, node1, node2)
            if k_clique_decision(G, k) is True:
                return k_clique(G, k)
            G = make_link(G, node1, node2)


if __name__ == '__main__':
    cases = [
        ({1: {}}, 1, [1]),
        ({1: {2: 1, 3: 1}, 2: {1: 1}, 3: {1: 1}}, 3, False),
        ({1: {2: 1, 3: 1, 4: 1}, 2: {1: 1, 4: 1}, 3: {1: 1}, 4: {1: 1, 2: 1}}, 3, [1, 2, 4]),
        ({1:{2:1, 3:1, 4:1}, 2:{1:1, 3:1, 4:1}, 3:{1:1, 2:1, 4:1}, 4:{1:1, 2:1, 3:1}}, 4, [1, 2, 3, 4])
    ]
    for G, k, expected in cases:
        print 'expected', expected
        print 'res', k_clique(G, k)