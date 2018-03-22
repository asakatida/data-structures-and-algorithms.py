def largest_product(array):
    if not array:
        return 0
    largest = array[0][0] * array[0][1]
    for i in range(1, len(array)):
        prod = array[i][0] * array[i][1]
        if prod > largest:
            largest = prod
    return largest
