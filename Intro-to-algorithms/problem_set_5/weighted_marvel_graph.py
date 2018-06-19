from itertools import combinations
from collections import defaultdict
import csv
import heapq


def dijkstra(G, v):

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
                new_dist = final_dist[w] + neighbours[x]
                if x not in dist_so_far or new_dist < dist_so_far[x]:
                    heapq.heappush(h, (new_dist, x))
                    dist_so_far[x] = new_dist
                    dist_path[x] = final_path[w]

    return final_path


def find_all_pathes(G, v):
    pathes = {v: [v]} # modification
    open_list = [v]
    while open_list:
        current = open_list.pop(0)
        for neighbor in G[current].keys():
            if neighbor not in pathes:  # modification
                pathes[neighbor] = pathes[current] + [neighbor]
                open_list.append(neighbor)
    return pathes


def read_graph(filename):
    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter='\t')
    book_characters = {}
    for (character, book) in tsv:
        book_characters.setdefault(book, []).append(character)
    return book_characters


def make_link(G, node1, node2):

    if node1 not in G:
        G[node1] = defaultdict(lambda: 0)
    G[node1][node2] += 1
    return G


def calculate_strength(characters_list):
    books = read_graph('../files/marvel_graph.tsv')
    G = defaultdict(int)
    counter = 0
    for book, characters in books.items():
        for c1, c2 in combinations(characters, 2):
            make_link(G, c1, c2)
            make_link(G, c2, c1)

    for c1 in G:
        G[c1] = {k: 1.0/v for k, v in G[c1].items()}
    for character in characters_list:
        path_with_weights = dijkstra(G, character)
        path_nodes = find_all_pathes(G, character)

        counter += sum([1 for c in path_nodes if len(path_with_weights[c]) > len(path_nodes[c])])
    return counter


characters_list = [
    'SPIDER-MAN/PETER PAR',
    'GREEN GOBLIN/NORMAN ',
    'WOLVERINE/LOGAN ',
    'PROFESSOR X/CHARLES ',
    'CAPTAIN AMERICA'
]
calculate_strength(characters_list)
