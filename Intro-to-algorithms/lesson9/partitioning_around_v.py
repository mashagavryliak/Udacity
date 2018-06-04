#
# Write partition to return a new array with 
# all values less then `v` to the left 
# and all values greater then `v` to the right
#


def partition(L, v):
    P = []
    right_part = []
    for val in L:
        if val < v:
            P.append(val)
        elif val > v:
            right_part.append(val)

    return P + [v] + right_part

L = [2, 5, 1, 10, 35, 80, 8]
print partition(L, 8)