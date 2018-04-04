from .fifo_animal_shelter import AnimalShelter
import pytest


@pytest.fixture
def new_queue():
    return AnimalShelter()


@pytest.fixture
def ordered_queue():
    return AnimalShelter(
        'dog' if i < 10 else 'cat' for i in range(3, 40, 3))


@pytest.fixture
def unordered_queue():
    return AnimalShelter(
        'dog' if i % 7 < 3 else 'cat' for i in range(73, 40, -2))


@pytest.fixture
def large_queue():
    return AnimalShelter('cat' for _ in range(0xFFFFFF))
