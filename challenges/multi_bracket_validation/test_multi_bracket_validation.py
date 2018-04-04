from .multi_bracket_validation import multi_bracket_validation


def test_valid_input():
    assert multi_bracket_validation('[hello world]')
