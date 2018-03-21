def getLength(array):
    count = 0
    for _ in array:
        count += 1
    return count


def getMiddleOfLength(length):
    return (length + 1) // 2


def yieldItemsWithItem(array, item, count, pos):
    insertCheck = False
    for i in range(count):
        if insertCheck:
            yield array[i - 1]
        elif i == pos:
            yield item
            insertCheck = True
        else:
            yield array[i]


def yieldItemsWithoutPos(array, count, pos):
    removeCheck = False
    for i in range(count):
        if removeCheck:
            yield array[i]
        elif i == pos:
            removeCheck = True
        else:
            yield array[i]


def insertShiftArray(array, item):
    count = getLength(array)
    pos = getMiddleOfLength(count)
    count += 1
    output = list(yieldItemsWithItem(array, item, count, pos))
    return output


def removeShiftArray(array):
    count = getLength(array)
    pos = count // 2
    output = list(yieldItemsWithoutPos(array, count, pos))
    return output
