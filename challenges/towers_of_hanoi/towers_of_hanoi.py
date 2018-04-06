from sys import argv


def towers_of_hanoi(n, start='A', end='C', spare='B'):
    """
    Generate the steps of towers of hanoi.
    """
    move = f'Disk { n } moved from { start } to { end }'
    if n == 1:
        return [move]
    return [
        *towers_of_hanoi(n - 1, start, spare, end),
        move,
        *towers_of_hanoi(n - 1, spare, end, start)]


def main():
    maximum = -1
    for move in towers_of_hanoi(int(argv[1])):
        m = int(move.split()[1])
        if m > maximum:
            maximum = m
            print(move)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
