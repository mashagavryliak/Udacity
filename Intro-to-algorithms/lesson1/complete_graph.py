#
# How many edges in a complete graph on n nodes?
#


def clique(n):
    # Return the number of edges
    return n*(n-1)/2

if __name__ == '__main__':
    print clique(10)
