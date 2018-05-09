def quicksort(array):
    """
    Sort an array using a recursive quicksort.
    """
    def _quick_help(array, start, end):
        if start >= end:
            return array
        right = end
        pivot = (end + start) // 2
        left = start
        while left < pivot or pivot < right:
            if left < pivot and array[pivot] < array[pivot - 1]:
                array[pivot - 1], array[pivot] = array[pivot], array[pivot - 1]
                pivot -= 1
            elif pivot < right and array[pivot + 1] < array[pivot]:
                array[pivot + 1], array[pivot] = array[pivot], array[pivot + 1]
                pivot += 1
            elif left < pivot and array[pivot] < array[left]:
                array[left], array[pivot - 1] = array[pivot - 1], array[left]
                left += 1
            elif pivot < right and array[right] < array[pivot]:
                array[right], array[pivot + 1] = array[pivot + 1], array[right]
                right -= 1
            else:
                left += 1
                right -= 1
        return _quick_help(
            _quick_help(
                array,
                start, pivot - 1),
            pivot + 1, end)

    array = list(array)
    return _quick_help(array, 0, len(array) - 1)
