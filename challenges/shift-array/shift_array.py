__all__ = ['getLength', 'getMiddleOfLength', 'insertShiftArray']

POISON_OBJECT = object()


def getLength(array):
    count = 0
    for _ in array:
        count += 1
    return count


def getMiddleOfLength(length):
    return (length + 1) // 2


def insertShiftArray(array, item):
    count = getLength(array)
    pos = getMiddleOfLength(count)
    count += 1
    output = [POISON_OBJECT for _ in range(count)]
    insertCheck = False
    for i in range(count):
        if insertCheck:
            output[i] = array[i - 1]
        elif i == pos:
            output[i] = item
            insertCheck = True
        else:
            output[i] = array[i]
    return output
