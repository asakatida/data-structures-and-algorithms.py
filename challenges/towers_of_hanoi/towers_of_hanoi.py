def towers_of_hanoi(n, start='A', end='C', spare='B'):
    """
    Generate the steps of towers of hanoi.
    """
    move = f'Disk { n } moved from { start } to { end }'
    if n == 1:
        return [move]
    result = towers_of_hanoi(n - 1, start, spare, end)
    result.append(move)
    result.extend(towers_of_hanoi(n - 1, spare, end, start))
    return result
