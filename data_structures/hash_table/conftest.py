from .hash_table import HashTable
from pytest import fixture


@fixture
def new_hash_table():
    return HashTable()


@fixture
def filled_hash_table():
    hash_table = HashTable()
    hash_table.set('None', 1)
    hash_table.set('1', 4)
    hash_table.set('1', 3)
    hash_table.set('1', 2)
    hash_table.set('2', 5)
    hash_table.set('4', 7)
    hash_table.set('4', 6)
    hash_table.set('5', 9)
    hash_table.set('5', 8)
    return hash_table
