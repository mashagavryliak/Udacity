"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    n = len(array)
    if n < 2:
        return array
    i, pos = 0, n-1
    while i < n-1 or pos < 0:
        if pos-i == 1:
            if array[i] > array[pos]:
                array[pos], array[i] = array[i], array[pos]
                pos -= 1
                break
        elif pos == i:
            break
        if array[i] > array[pos]:
            array[pos], array[pos-1], array[i] = array[i], array[pos], array[pos-1]
            pos -= 1
        else:
            i += 1
    return quicksort(array[:pos]) + array[pos:pos+1] + quicksort(array[pos+1:])


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)