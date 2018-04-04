from .stack import Stack


def multi_bracket_validation(input):
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
