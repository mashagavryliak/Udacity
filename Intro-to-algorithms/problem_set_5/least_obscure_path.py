import csv
import heapq
from collections import defaultdict
from itertools import combinations


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
                new_dist = max(final_dist[w], neighbours[x])
                if x not in dist_so_far or new_dist < dist_so_far[x]:
                    heapq.heappush(h, (new_dist, x))
                    dist_so_far[x] = new_dist

    return final_dist


def make_link(G, node1, node2, weight):
    G[node1][node2] = max(weight, G[node1].get(node2, 0))
    G[node2][node1] = max(weight, G[node2].get(node1, 0))
    return G


def form_graph():
    tsv = csv.reader(open('../files/imdb-weights.tsv'), delimiter='\t')
    weights = {}
    for movie, year, score in tsv:
        weights['{} {}'.format(movie, year)] = float(score)

    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open('../files/imdb-1.tsv'), delimiter='\t')
    G = defaultdict(dict)
    movie_actors = defaultdict(list)
    for actor, movie, year in tsv:
        movie_actors['{} {}'.format(movie, year)].append(actor)
    for movie in movie_actors:
        for actor1, actor2 in combinations(movie_actors[movie], 2):
            make_link(G, actor1, actor2, weights[movie])
    return G


test_data = {(u'Ali, Tony', u'Allen, Woody'): 0.5657,
        (u'Auberjonois, Rene', u'MacInnes, Angus'): 0.0814,
        (u'Avery, Shondrella', u'Dorsey, Kimberly (I)'): 0.7837,
        (u'Bollo, Lou', u'Jeremy, Ron'): 0.4763,
        (u'Byrne, P.J.', u'Clarke, Larry'): 0.109,
        (u'Couturier, Sandra-Jessica', u'Jean-Louis, Jimmy'): 0.3649,
        (u'Crawford, Eve (I)', u'Cutler, Tom'): 0.2052,
        (u'Flemyng, Jason', u'Newman, Laraine'): 0.139,
        (u'French, Dawn', u'Smallwood, Tucker'): 0.2979,
        (u'Gunton, Bob', u'Nagra, Joti'): 0.2136,
        (u'Hoffman, Jake (I)', u'Shook, Carol'): 0.6073,
        # (u'Kamiki, Ry\xfbnosuke', u'Thor, Cameron'): 0.3644,
        (u'Roache, Linus', u'Dreyfuss, Richard'): 0.6731,
        (u'Sanchez, Phillip (I)', u'Wiest, Dianne'): 0.5083,
        (u'Sheppard, William Morgan', u'Crook, Mackenzie'): 0.0849,
        (u'Stan, Sebastian', u'Malahide, Patrick'): 0.2857,
        (u'Tessiero, Michael A.', u'Molen, Gerald R.'): 0.2056,
        (u'Thomas, Ken (I)', u'Bell, Jamie (I)'): 0.3941,
        (u'Thompson, Sophie (I)', u'Foley, Dave (I)'): 0.1095,
        (u'Tzur, Mira', u'Heston, Charlton'): 0.3642}

answer = {(u'Boone Junior, Mark', u'Del Toro, Benicio'): None,
          (u'Braine, Richard', u'Coogan, Will'): None,
          (u'Byrne, Michael (I)', u'Quinn, Al (I)'): None,
          (u'Cartwright, Veronica', u'Edelstein, Lisa'): None,
          (u'Curry, Jon (II)', u'Wise, Ray (I)'): None,
          (u'Di Benedetto, John', u'Hallgrey, Johnathan'): None,
          (u'Hochendoner, Jeff', u'Cross, Kendall'): None,
          (u'Izquierdo, Ty', u'Kimball, Donna'): None,
          (u'Jace, Michael', u'Snell, Don'): None,
          (u'James, Charity', u'Tuerpe, Paul'): None,
          (u'Kay, Dominic Scott', u'Cathey, Reg E.'): None,
          (u'McCabe, Richard', u'Washington, Denzel'): None,
          (u'Reid, Kevin (I)', u'Affleck, Rab'): None,
          (u'Reid, R.D.', u'Boston, David (IV)'): None,
          (u'Restivo, Steve', u'Preston, Carrie (I)'): None,
          (u'Rodriguez, Ramon (II)', u'Mulrooney, Kelsey'): None,
          (u'Rooker, Michael (I)', u'Grady, Kevin (I)'): None,
          (u'Ruscoe, Alan', u'Thornton, Cooper'): None,
          (u'Sloan, Tina', u'Dever, James D.'): None,
          (u'Wasserman, Jerry', u'Sizemore, Tom'): None}


def test():
    G = form_graph()
    for nodes, expected in test_data.items():
        assert dijkstra(G, nodes[0])[nodes[1]] == expected

    for nodes in answer:
        print nodes, dijkstra(G, nodes[0])[nodes[1]]


test()
