from itertools import chain, islice, repeat, tee


def mergesort(array):
    """
    Sort an array using an iterative mergesort.
    """
    array = list(array)
    len_array = len(array)
    max_index = repeat(len_array - 1)
    step = 1
    while step < len_array:
        odd, even = tee(range(0, len_array, step))
        for s in zip(islice(odd, 0, None, 2), islice(even, 1, None, 2)):
            ks = chain(range(s[1], len_array), max_index)
            k = next(ks)
            for j in range(*s):
                if array[k] < array[j]:
                    array[k], array[j] = array[j], array[k]
                    k = next(ks)
        step <<= 1
    return array
