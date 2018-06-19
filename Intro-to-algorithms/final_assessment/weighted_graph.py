#
# In lecture, we took the bipartite Marvel graph,
# where edges went between characters and the comics
# books they appeared in, and created a weighted graph
# with edges between characters where the weight was the
# number of comic books in which they both appeared.
#
# In this assignment, determine the weights between
# comic book characters by giving the probability
# that a randomly chosen comic book containing one of
# the characters will also contain the other
#
from itertools import combinations
from collections import defaultdict
from marvel import marvel, characters


def create_weighted_graph(bipartiteG, characters):
    G = defaultdict(dict)
    for c1, c2 in combinations(characters, 2):
        c1_books = set(bipartiteG[c1])
        c2_books = set(bipartiteG[c2])
        score = 1.0*len(c1_books & c2_books) / len(c1_books | c2_books)
        if score > 0:
            G[c1][c2] = score
            G[c2][c1] = score
    return G


def test():
    bipartiteG = {'charA': {'comicB': 1, 'comicC': 1},
                  'charB': {'comicB': 1, 'comicD': 1},
                  'charC': {'comicD': 1},
                  'comicB': {'charA': 1, 'charB': 1},
                  'comicC': {'charA': 1},
                  'comicD': {'charC': 1, 'charB': 1}}
    G = create_weighted_graph(bipartiteG, ['charA', 'charB', 'charC'])
    # three comics contain charA or charB
    # charA and charB are together in one of them
    assert G['charA']['charB'] == 1.0 / 3
    assert G['charA'].get('charA') == None
    assert G['charA'].get('charC') == None


def test2():
    G = create_weighted_graph(marvel, characters)

