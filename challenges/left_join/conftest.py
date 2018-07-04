from pytest import fixture

from data_structures.hash_table.hash_table import HashTable


@fixture
def abcd_table1():
    """
    """
    hash_table = HashTable()
    hash_table.set("a", object())
    hash_table.set("b", object())
    hash_table.set("c", object())
    hash_table.set("d", object())
    return hash_table


@fixture
def abcd_table2():
    """
    """
    hash_table = HashTable()
    hash_table.set("a", object())
    hash_table.set("b", object())
    hash_table.set("c", object())
    hash_table.set("d", object())
    return hash_table


@fixture
def efgh_table():
    """
    """
    hash_table = HashTable()
    hash_table.set("e", object())
    hash_table.set("f", object())
    hash_table.set("g", object())
    hash_table.set("h", object())
    return hash_table


@fixture
def aceg_table():
    """
    """
    hash_table = HashTable()
    hash_table.set("a", object())
    hash_table.set("c", object())
    hash_table.set("e", object())
    hash_table.set("g", object())
    return hash_table


@fixture
def empty_table():
    """
    """
    return HashTable()
