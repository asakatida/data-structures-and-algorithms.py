def binary_search(array, key):
    bound_high = len(array)
    bound_low = 0
    index = 0
    while True:
        new_pos = bound_low + (bound_high - bound_low) // 2
        if new_pos == index:
            return -1
        index = new_pos
        if array[index] == key:
            return index
        elif array[index] < key:
            bound_low = index + 1
        else:
            bound_high = index - 1
