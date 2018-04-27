from .fifo_animal_shelter import AnimalShelter, Cat, Dog
from pytest import fixture


@fixture
def new_queue():
    return AnimalShelter()


@fixture
def ordered_queue():
    return AnimalShelter(
        Dog() if i < 10 else Cat() for i in range(3, 40, 3))


@fixture
def unordered_queue():
    return AnimalShelter(
        Dog() if i % 7 < 3 else Cat() for i in range(73, 40, -2))


@fixture
def large_queue():
    return AnimalShelter(Cat() for _ in range(0xFFFFFF))
