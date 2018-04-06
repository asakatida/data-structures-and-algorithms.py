from sys import argv


def towers_of_hanoi(n, start='A', end='C', spare='B'):
    """
    Generate the steps of towers of hanoi.
    """
    output = []
    if n == 1:
        output.append(f'Disk { n } moved from { start } to { end }')
    else:
        output.extend(towers_of_hanoi(n - 1, start, spare, end))
        output.append(f'Disk { n } moved from { start } to { end }')
        output.extend(towers_of_hanoi(n - 1, spare, end, start))
    return output


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
