from .towers_of_hanoi import towers_of_hanoi


def test_towers_of_hanoi_1():
    assert len(list(towers_of_hanoi(1))) == 1


def test_towers_of_hanoi_2():
    assert len(list(towers_of_hanoi(2))) == 3


def test_towers_of_hanoi_3():
    assert len(list(towers_of_hanoi(3))) == 7


def test_towers_of_hanoi_4():
    assert len(list(towers_of_hanoi(4))) == 15
