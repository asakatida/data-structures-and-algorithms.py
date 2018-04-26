from .stack import Stack


def towers_of_hanoi_list(n):
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


class _Move:
    def __init__(self, disk, start='A', end='C', spare='B'):
        self.disk = disk
        self.start = start
        self.end = end
        self.spare = spare

    def __str__(self):
        return f'Disk { self.disk } moved from { self.start } to { self.end }'


def towers_of_hanoi(n):
    """
    Generate the steps of towers of hanoi.
    """
    stack = Stack([_Move(n)])
    while stack:
        move = stack.pop()
        if isinstance(move, _Move):
            if move.disk == 1:
                yield str(move)
            else:
                stack.push(
                    _Move(move.disk - 1, move.spare, move.end, move.start))
                stack.push(str(move))
                stack.push(
                    _Move(move.disk - 1, move.start, move.spare, move.end))
        else:
            yield move
