from itertools import chain, islice, repeat, tee


def sort_range(array, start, end):
    """
    Sort an array slice using an iterative mergesort.
    """
    mid = (start + end) // 2
    ks = chain(range(mid, end), repeat(end))
    k = next(ks)
    for j in range(start, mid):
        while array[k] < array[j]:
            array[k], array[j] = array[j], array[k]
            k = next(ks)


def mergesort(array):
    """
    Sort an array using an iterative mergesort.
    """
    array = list(array)
    len_array = len(array)
    max_index = len_array - 1
    step = 1
    while step < len_array:
        steps = tee(chain(range(0, len_array, step), [max_index]))
        odd = chain(islice(steps[0], 0, None, 2), [max_index])
        even = chain(islice(steps[1], 1, None, 2), [max_index])
        for start, end in zip(odd, even):
            sort_range(array, start, end)
        step <<= 1
    sort_range(array, 0, len_array)
    return array
