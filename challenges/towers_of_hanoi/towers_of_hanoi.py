def towers_of_hanoi(n, start='A', end='C', spare='B'):
    """
    Generate the steps of towers of hanoi.
    """
    if n == 1:
        yield f'Disk { n } moved from { start } to { end }'
    else:
        yield from towers_of_hanoi(n - 1, start, spare, end)
        yield f'Disk { n } moved from { start } to { end }'
        yield from towers_of_hanoi(n - 1, spare, end, start)
