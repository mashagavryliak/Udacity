#
# Design and implement an algorithm that can preprocess a
# graph and then answer the question "is x connected to y in the
# graph" for any x and y in constant time Theta(1).
#

#
# `process_graph` will be called only once on each graph.  If you want,
# you can store whatever information you need for `is_connected` in
# global variables
#
import heapq


preprocessed_graph = {}


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


def process_graph(G):
    global preprocessed_graph
    preprocessed_graph = {}
    for node in G.keys():
        preprocessed_graph[node] = {x for x in dijkstra(G, node)}

#
# When being graded, `is_connected` will be called
# many times so this routine needs to be quick


def is_connected(i, j):
    global preprocessed_graph
    return j in preprocessed_graph[i]

#######
# Testing
#
def test():
    G = {'a':{'b':1},
         'b':{'a':1},
         'c':{'d':1},
         'd':{'c':1},
         'e':{}}
    process_graph(G)
    assert is_connected('a', 'b') == True
    assert is_connected('a', 'c') == False

    G = {'a':{'b':1, 'c':1},
         'b':{'a':1},
         'c':{'d':1, 'a':1},
         'd':{'c':1},
         'e':{}}
    process_graph(G)
    assert is_connected('a', 'b') == True
    assert is_connected('a', 'c') == True
    assert is_connected('a', 'e') == False


test()

