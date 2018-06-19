#
# Take a weighted graph representing a social network where the weight
# between two nodes is the "love" between them.  In this "feel the
# love of a path" problem, we want to find the best path from node `i`
# and node `j` where the score for a path is the maximum love of an
# edge on this path. If there is no path from `i` to `j` return
# `None`.  The returned path doesn't need to be simple, ie it can
# contain cycles or repeated vertices.
#
# Devise and implement an algorithm for this problem.
#
import heapq


def dijkstra_path(G, v):

    final_dist = {}
    dist_so_far = {v: 0}
    h = [(0, v)]
    dist_path = {v: []}
    final_path = {}
    while dist_so_far:
        # get shortest distance
        d, w = heapq.heappop(h)
        if w in final_dist or d > dist_so_far[w]:
            continue
        final_dist[w] = d
        # if w != v:
        final_path[w] = dist_path[w] + [w]
        del dist_so_far[w]
        neighbours = G[w]
        for x in neighbours:
            if x not in final_dist:
                new_dist = max(final_dist[w], neighbours[x])
                if x not in dist_so_far or new_dist < dist_so_far[x]:
                    heapq.heappush(h, (new_dist, x))
                    dist_so_far[x] = new_dist
                    dist_path[x] = final_path[w]

    return final_path


def feel_the_love(G, i, j):
    pathes_form_start = dijkstra_path(G, i)
    if j not in pathes_form_start:
        return None
    pathes_to_end = dijkstra_path(G, j)
    edges = {}
    for node1 in G:
        for node2 in G[node1]:
            if (node1, node2) not in edges and (node2, node1) not in edges:
                edges[(node1, node2)] = G[node1][node2]

    edges_sorted = sorted(edges, key=edges.get, reverse=True)
    for edge in edges_sorted:
        node1, node2 = edge
        if node1 in pathes_form_start and node2 in pathes_to_end:
            return pathes_form_start[node1] + pathes_to_end[node2][::-1]
        if node2 in pathes_form_start and node1 in pathes_to_end:
            return pathes_form_start[node2] + pathes_to_end[node1][::-1]

#########
#
# Test

def score_of_path(G, path):
    max_love = -float('inf')
    for n1, n2 in zip(path[:-1], path[1:]):
        love = G[n1][n2]
        if love > max_love:
            max_love = love
    return max_love


def test():
    G = {'a': {'c': 1},
         'b': {'c': 1},
         'c': {'a': 1, 'b': 1, 'e': 1, 'd': 1},
         'e': {'c': 1, 'd': 2},
         'd': {'e': 2, 'c': 1},
         'f': {}}
    path = feel_the_love(G, 'a', 'b')
    assert score_of_path(G, path) == 2

    path = feel_the_love(G, 'a', 'f')
    assert path == None


if __name__ == '__main__':
    test()


