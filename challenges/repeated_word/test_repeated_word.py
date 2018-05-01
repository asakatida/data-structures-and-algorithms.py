from .repeated_word import repeated_word


def test_empty_string_repeated_word():
    assert repeated_word('') is None


def test_no_repeat_repeated_word():
    assert repeated_word('') is None


def test_repeat_start_repeated_word():
    assert repeated_word('') is None


def test_repeat_end_repeated_word():
    assert repeated_word('') is None


def test_repeat_middle_repeated_word():
    assert repeated_word('') is None
