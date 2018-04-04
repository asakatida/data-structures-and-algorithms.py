from .stack import Stack


def multi_bracket_validation(input):
    """
    Test input string for matching brackets.

    Valid input look as follows:
    - `[[[[]]]]`
    - `[][]{}`
    - `{()}({})`

    Invalid inputs could be as follows:
    - `(()}`
    - `}}`
    - `][`
    """
    openers = Stack()
    for c in input:
        if c in '[({':
            openers.push(c)
        elif c == ']':
            if not openers:
                return False
            if openers.pop() != '[':
                return False
        elif c == ')':
            if not openers:
                return False
            if openers.pop() != '(':
                return False
        elif c == '}':
            if not openers:
                return False
            if openers.pop() != '{':
                return False
    return not openers
