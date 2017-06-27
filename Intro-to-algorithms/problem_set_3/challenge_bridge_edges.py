# Bridge Edges v4
#
# Find the bridge edges in a graph given the
# algorithm in lecture.
# Complete the intermediate steps
#  - create_rooted_spanning_tree
#  - post_order
#  - number_of_descendants
#  - lowest_post_order
#  - highest_post_order
#
# And then combine them together in
# `bridge_edges`

# So far, we've represented graphs
# as a dictionary where G[n1][n2] == 1
# meant there was an edge between n1 and n2
#
# In order to represent a spanning tree
# we need to create two classes of edges
# we'll refer to them as "green" and "red"
# for the green and red edges as specified in lecture
#
# So, for example, the graph given in lecture
# G = {'a': {'c': 1, 'b': 1},
#      'b': {'a': 1, 'd': 1},
#      'c': {'a': 1, 'd': 1},
#      'd': {'c': 1, 'b': 1, 'e': 1},
#      'e': {'d': 1, 'g': 1, 'f': 1},
#      'f': {'e': 1, 'g': 1},
#      'g': {'e': 1, 'f': 1}
#      }
# would be written as a spanning tree
# S = {'a': {'c': 'green', 'b': 'green'},
#      'b': {'a': 'green', 'd': 'red'},
#      'c': {'a': 'green', 'd': 'green'},
#      'd': {'c': 'green', 'b': 'red', 'e': 'green'},
#      'e': {'d': 'green', 'g': 'green', 'f': 'green'},
#      'f': {'e': 'green', 'g': 'red'},
#      'g': {'e': 'green', 'f': 'red'}
#      }
#


def parameter_calculation(S, root, func, po={}):

    scores = {}
    tree = {}
    for node in S:
        tree[node] = {k: v for k, v in S[node].items() if v == 'green'}
    while len(scores) < len(S) - 1:
        nodes = tree.keys()
        for node in nodes:
            connections = [k for k, v in tree[node].items() if k not in scores]
            if len(connections) == 1 and node != root:
                func(S=S, node=node, tree=tree, scores=scores, po=po)
    func(S=S, node=root, tree=tree, scores=scores, po=po)
    return scores

def create_rooted_spanning_tree(G, root):

    S = {node: {} for node in G}
    nodes = [root]
    while nodes:
        node = nodes.pop(0)
        for neighbour in G[node]:
            # create green connection if there was no before
            if S[neighbour] == {}:
                S[node][neighbour] = 'green'
                S[neighbour][node] = 'green'
                nodes.append(neighbour)
            else:
                S[node][neighbour] = S[neighbour].get(node, 'red')
    return S


# This is just one possible solution
# There are other ways to create a
# spanning tree, and the grader will
# accept any valid result
# feel free to edit the test to
# match the solution your program produces
def test_create_rooted_spanning_tree():
    G = {'a': {'c': 1, 'b': 1},
         'b': {'a': 1, 'd': 1},
         'c': {'a': 1, 'd': 1},
         'd': {'c': 1, 'b': 1, 'e': 1},
         'e': {'d': 1, 'g': 1, 'f': 1},
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1}
         }
    S = create_rooted_spanning_tree(G, "a")
    assert S == {'a': {'c': 'green', 'b': 'green'},
                 'b': {'a': 'green', 'd': 'red'},
                 'c': {'a': 'green', 'd': 'green'},
                 'd': {'c': 'green', 'b': 'red', 'e': 'green'},
                 'e': {'d': 'green', 'g': 'green', 'f': 'green'},
                 'f': {'e': 'green', 'g': 'red'},
                 'g': {'e': 'green', 'f': 'red'}
                 }


###########

def post_order(S, root):

    def po_calculation(**kwargs):
        node, tree, scores = kwargs['node'], kwargs['tree'], kwargs['scores']
        score = 0
        if scores:
            score = max(scores.values())
        scores[node] = score + 1
        del tree[node]

    return parameter_calculation(S, root, po_calculation)


# This is just one possible solution
# There are other ways to create a
# spanning tree, and the grader will
# accept any valid result.
# feel free to edit the test to
# match the solution your program produces
def test_post_order():
    S = {'a': {'c': 'green', 'b': 'green'},
         'b': {'a': 'green', 'd': 'red'},
         'c': {'a': 'green', 'd': 'green'},
         'd': {'c': 'green', 'b': 'red', 'e': 'green'},
         'e': {'d': 'green', 'g': 'green', 'f': 'green'},
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'}
         }
    po = post_order(S, 'a')
    assert po == {'a': 7, 'b': 1, 'c': 6, 'd': 5, 'e': 4, 'f': 3, 'g': 2}


##############

def number_of_descendants(S, root):
    # return mapping between nodes of S and the number of descendants
    # of that node
    def descendants_calculation(**kwargs):
        node, tree, scores = kwargs['node'], kwargs['tree'], kwargs['scores']
        scores[node] = 1 + sum(scores.get(k, 0) for k in tree[node])
        del tree[node]

    return parameter_calculation(S, root, descendants_calculation)


def test_number_of_descendants():
    S = {'a': {'c': 'green', 'b': 'green'},
         'b': {'a': 'green', 'd': 'red'},
         'c': {'a': 'green', 'd': 'green'},
         'd': {'c': 'green', 'b': 'red', 'e': 'green'},
         'e': {'d': 'green', 'g': 'green', 'f': 'green'},
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'}
         }
    nd = number_of_descendants(S, 'a')
    assert nd == {'a': 7, 'b': 1, 'c': 5, 'd': 4, 'e': 3, 'f': 1, 'g': 1}


###############

def lowest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the lowest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    def lowest_calculation(**kwargs):
        node, tree, scores, po = kwargs['node'], kwargs['tree'], kwargs['scores'], kwargs['po']
        lowest = [scores[x] for x in S[node] if x in scores]
        lowest.append(po[node])
        scores[node] = min(lowest)
        del tree[node]
        red_connections = [k for k, v in S[node].items() if k in scores and v == 'red']
        if red_connections:
            scores[node] = min(scores[node], scores[red_connections[0]])

    return parameter_calculation(S, root, lowest_calculation, po)



def test_lowest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'},
         'b': {'a': 'green', 'd': 'red'},
         'c': {'a': 'green', 'd': 'green'},
         'd': {'c': 'green', 'b': 'red', 'e': 'green'},
         'e': {'d': 'green', 'g': 'green', 'f': 'green'},
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'}
         }
    po = post_order(S, 'a')
    l = lowest_post_order(S, 'a', po)
    assert l == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 2, 'f': 2, 'g': 2}


################

def highest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the highest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    def highest_calculation(**kwargs):
        node, tree, scores, po = kwargs['node'], kwargs['tree'], kwargs['scores'], kwargs['po']
        highest = [scores[x] for x in S[node] if x in scores]
        highest.append(po[node])
        scores[node] = max(highest)
        del tree[node]
        red_connections = [k for k, v in S[node].items() if k in scores and v == 'red']
        if red_connections:
            scores[node] = max(scores[node], scores[red_connections[0]])
            scores[red_connections[0]] = max(scores[node], scores[red_connections[0]])

    return parameter_calculation(S, root, highest_calculation, po)


def test_highest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'},
         'b': {'a': 'green', 'd': 'red'},
         'c': {'a': 'green', 'd': 'green'},
         'd': {'c': 'green', 'b': 'red', 'e': 'green'},
         'e': {'d': 'green', 'g': 'green', 'f': 'green'},
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'}
         }
    po = post_order(S, 'a')
    h = highest_post_order(S, 'a', po)
    assert h == {'a': 7, 'b': 5, 'c': 6, 'd': 5, 'e': 4, 'f': 3, 'g': 3}


#################

def bridge_edges(G, root):
    # use the four functions above
    # and then determine which edges in G are bridge edges
    # return them as a list of tuples ie: [(n1, n2), (n4, n5)]
    def check_if_bridge(node):
        del tree[node]
        passed.append(node)
        if h[node] <= po[node]:
            if l[node] > po[node] - nd[node]:
                return 1
        return 0
    S = create_rooted_spanning_tree(G, root)
    po = post_order(S, root)
    nd = number_of_descendants(S, root)
    l = lowest_post_order(S, root, po)
    h = highest_post_order(S, root, po)

    passed = []
    bridges = []
    tree = {}
    for node in S:
        tree[node] = {k: v for k, v in S[node].items() if v == 'green'}
    while len(passed) < len(S) - 1:
        nodes = tree.keys()
        for node in nodes:
            connections = [k for k, v in tree[node].items() if k not in passed]
            if len(connections) == 1 and node != root:
                if check_if_bridge(node):
                    bridges.append((connections[0], node))
    return bridges



def test_bridge_edges():
    G = {'a': {'c': 1, 'b': 1},
         'b': {'a': 1, 'd': 1},
         'c': {'a': 1, 'd': 1},
         'd': {'c': 1, 'b': 1, 'e': 1},
         'e': {'d': 1, 'g': 1, 'f': 1},
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1}
         }
    bridges = bridge_edges(G, 'a')
    assert bridges == [('d', 'e')]

if __name__ == '__main__':
    test_create_rooted_spanning_tree()
    test_post_order()
    test_number_of_descendants()
    test_lowest_post_order()
    test_highest_post_order()
    test_bridge_edges()
