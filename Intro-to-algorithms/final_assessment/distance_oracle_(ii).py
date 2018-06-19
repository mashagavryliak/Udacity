#
# This is the same problem as "Distance Oracle I" except that instead of
# only having to deal with binary trees, the assignment asks you to
# create labels for all tree graphs.
#
# In the shortest-path oracle described in Andrew Goldberg's
# interview, each node has a label, which is a list of some other
# nodes in the network and their distance to these nodes.  These lists
# have the property that
#
#  (1) for any pair of nodes (x,y) in the network, their lists will
#  have at least one node z in common
#
#  (2) the shortest path from x to y will go through z.
#
# Given a graph G that is a tree, preprocess the graph to
# create such labels for each node.  Note that the size of the list in
# each label should not be larger than log n for a graph of size n.
#

#
# create_labels takes in a tree and returns a dictionary, mapping each
# node to its label
#
# a label is a dictionary mapping another node and the distance to
# that node
import heapq
from collections import defaultdict
from copy import deepcopy


def create_labels(tree):
    labels = defaultdict(dict)
    tree_copy = deepcopy(tree)
    add_subtree_labels(tree_copy, labels)
    return labels


def add_subtree_labels(tree, labels):

    if len(tree) == 1:
        node = tree.keys()[0]
        labels[node][node] = 0
        return labels

    root = find_root(tree)
    dist = dijkstra(tree, root)
    for node in dist:
        labels[node][root] = dist[node]

    tree = delete_root_edges(tree, root)
    for subtree in build_subtrees(tree):
        add_subtree_labels(subtree, labels)
    return labels


def build_subtrees(old_tree):
    subtrees = []
    used_nodes = []
    node_list = old_tree.keys()
    while node_list:
        node = node_list.pop(0)
        if node in used_nodes:
            continue
        new_tree = {}
        tree_members = dijkstra(old_tree, node).keys()
        for n in tree_members:
            new_tree[n] = old_tree[n]
            used_nodes.append(n)
        subtrees.append(new_tree)
    return subtrees


def delete_root_edges(tree, root):
    neighbours = tree[root].keys()
    while neighbours:
        neighbour = neighbours.pop(0)
        tree.get(neighbour).pop(root)
    del tree[root]
    return tree

def dijkstra(G, v):

    final_dist = {}
    dist_so_far = {v: 0}
    h = [(0, v)]
    while dist_so_far:
        # get shortest distance
        d, w = heapq.heappop(h)
        if w in final_dist or d > dist_so_far[w]:
            continue
        final_dist[w] = d
        del dist_so_far[w]
        neighbours = G[w]
        for x in neighbours:
            if x not in final_dist:
                new_dist = final_dist[w] + neighbours[x]
                if x not in dist_so_far or new_dist < dist_so_far[x]:
                    heapq.heappush(h, (new_dist, x))
                    dist_so_far[x] = new_dist

    return final_dist


def find_root(tree):
    tree_copy = deepcopy(tree)
    while tree_copy:
        leaves = [node for node in tree_copy if len(tree_copy[node]) < 2]
        for node, neighbours in tree_copy.items():
            tree_copy[node] = {k: v for k, v in neighbours.items() if k not in leaves}
        tree_copy = {k: v for k, v in tree_copy.items() if k not in leaves}
    return leaves[0]

#######
# Testing
#


def get_distances(G, labels):
    # labels = {a:{b: distance from a to b,
    #              c: distance from a to c}}
    # create a mapping of all distances for
    # all nodes
    distances = {}
    for start in G:
        # get all the labels for my starting node
        label_node = labels[start]
        s_distances = {}
        for destination in G:
            shortest = float('inf')
            # get all the labels for the destination node
            label_dest = labels[destination]
            # and then merge them together, saving the
            # shortest distance
            for intermediate_node, dist in label_node.iteritems():
                # see if intermediate_node is our destination
                # if it is we can stop - we know that is
                # the shortest path
                if intermediate_node == destination:
                    shortest = dist
                    break
                other_dist = label_dest.get(intermediate_node)
                if other_dist is None:
                    continue
                if other_dist + dist < shortest:
                    shortest = other_dist + dist
            s_distances[destination] = shortest
        distances[start] = s_distances
    return distances


def make_link(G, node1, node2, weight=1):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = weight
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = weight
    return G


def test():
    edges = [(1, 2), (2, 3), (2, 4), (2, 5), (3, 6), (3, 7),
             (4, 8), (4, 9), (5, 10), (5, 11), (6, 12), (6, 13)]
    tree = {}
    for n1, n2 in edges:
        make_link(tree, n1, n2)
    labels = create_labels(tree)
    print tree
    print labels
    distances = get_distances(tree, labels)
    assert distances[1][2] == 1
    assert distances[1][4] == 2


test()



