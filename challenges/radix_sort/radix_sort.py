from math import ceil, log10, log2


def radix_sort(array, radix=None):
    """
    Sort an array using a radix sort.
    """
    def _linear(buckets):
        for bucket in buckets:
            yield from bucket
    def _radix_help(buckets, digit, radix):
        new = [[] for _ in range(radix * 2)]
        for i in _linear(buckets):
            bucket = (i // (radix ** digit)) % radix
            if i >= 0:
                bucket += radix
            new[bucket].append(i)
        return new

    _array = []
    is_sorted = True
    max_digit = 0
    for i in array:
        if is_sorted and _array:
            is_sorted = _array[-1] <= i
        if max_digit < abs(i):
            max_digit = abs(i)
        _array.append(i)
    if is_sorted:
        return _array
    buckets = [_array]
    max_digit = ceil(log10(max_digit)) + 1
    if not isinstance(radix, int):
        radix = max_digit + 2
    for digit in range(max_digit):
        buckets = _radix_help(buckets, digit, radix)
    return list(_linear(buckets))
