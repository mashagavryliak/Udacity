from itertools import combinations
from collections import defaultdict
import csv


def read_graph(filename):
    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter='\t')
    book_characters = {}
    for (character, book) in tsv:
        book_characters.setdefault(book, []).append(character)
    return book_characters


def calculate_strength():
    books = read_graph('../files/marvel_graph.tsv')
    G = defaultdict(int)
    for book, characters in books.items():
        for c1, c2 in combinations(characters, 2):
            c1, c2 = sorted([c1, c2])
            G['%s vs %s' % (c1, c2)] += 1

    print max(G.items(), key=lambda x: x[1])


calculate_strength()

