import csv


def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G


def read_graph(filename):
    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter='\t')
    G = {}
    actors = set([])
    for row in tsv:
        node1 = row[0]
        node2 = ' '.join(row[1:])
        actors.add(node1)
        make_link(G, node1, node2)
    return G, actors


def centrality(G, v):
    distance_from_start = {}
    open_list = [v]
    distance_from_start[v] = 0
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                open_list.append(neighbor)
    return float(sum(distance_from_start.values()))/len(distance_from_start)

def calculate_top_actors():
    centralities = {}
    G, actors = read_graph('file.tsv')
    for actor in actors:
        centralities[actor] = centrality(G, actor)

    sorted_actors = sorted(centralities.items(), key=lambda x: x[1])[:20]
    print 'first:', sorted_actors[0]
    print '20th:', sorted_actors[19]


calculate_top_actors()
