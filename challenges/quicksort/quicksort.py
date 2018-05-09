def quicksort(array):
    """
    Sort an array using a recursive quicksort.
    """
    def _quick_help(array, start, end):
        pivot = end - 1
        right = pivot - 1
        left = start
        if pivot <= left:
            return array
        while left < pivot:
            if array[pivot] < array[right]:
                array[pivot], array[right] = array[right], array[pivot]
                pivot -= 1
                right -= 1
            elif array[pivot] < array[left]:
                array[left], array[right] = array[right], array[left]
                left += 1
            else:
                left += 1
        return _quick_help(
            _quick_help(
                array,
                start, pivot),
            pivot + 1, end)

    array = list(array)
    return _quick_help(array, 0, len(array))
