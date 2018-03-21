def insertShiftArray(array, item):
    count = 0
    for _ in array:
        count += 1
    count += 1
    pos = count // 2
    output = [None for _ in range(count)]
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
