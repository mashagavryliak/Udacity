def find_eulerian_tour(graph):
    pathed_edges = []
    a = graph[0][0]
    s = [a]
    c = []
    while len(s) > 0:
        x = s[-1]
        available_edges = [e for e in graph if e not in pathed_edges and x in e]
        if available_edges:
            edge = available_edges[0]
            pathed_edges.append(edge)
            if edge[0] == x:
                s.append(edge[1])
            else:
                s.append(edge[0])
        else:
            c.append(x)
            del s[-1]
    return c


graph = [(1, 2), (2, 3), (3, 1)]
print find_eulerian_tour(graph)
graph = [(0, 1), (1, 5), (1, 7), (4, 5),
(4, 8), (1, 6), (3, 7), (5, 9),
(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
print find_eulerian_tour(graph)
graph = [(1, 13), (1, 6), (6, 11), (3, 13),
(8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9),
(1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9),
(7, 14),  (10, 13)]
print find_eulerian_tour(graph)
graph = [(8, 16), (8, 18), (16, 17), (18, 19),
(3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14),
(1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15),
(6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)]
print find_eulerian_tour(graph)