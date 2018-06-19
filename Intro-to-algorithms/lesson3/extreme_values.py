#
# Write `max`
#


def max(L):
    max_v = L[0]
    for el in L[1:]:
        if el > max_v:
            max_v = el
    return max_v


def test():
    L = [1, 2, 3, 4]
    assert 4 == max(L)
    L = [3, 6, 10, 9, 3]
    assert 10 == max(L)

test()


