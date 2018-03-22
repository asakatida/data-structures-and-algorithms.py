def adjacent_positions(array, i, j):
    if i + 1 < len(array):
        yield array[i + 1][j]
    if i - 1 > 0:
        yield array[i - 1][j]
    row = array[i]
    if j + 1 < len(row):
        yield row[j + 1]
    if j - 1 > 0:
        yield row[j - 1]


def largest_adjacent_product(array, i, j):
    target = array[i][j]
    largest = 0
    for adjacent in adjacent_positions(array, i, j):
        prod = target * adjacent
        print('largest_adjacent_product', i, j, prod)
        if prod > largest:
            largest = prod
    return largest


def largest_product(array):
    if not array:
        return 0
    largest = 0
    for i in range(len(array)):
        for j in range(i % 2, len(array[i]), 2):
            prod = largest_adjacent_product(array, i, j)
            print('largest_product', i, j, prod)
            if prod > largest:
                largest = prod
    print('largest_product', largest)
    return largest
