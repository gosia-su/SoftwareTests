def add(x, y):
    return x + y


def test_add():
    assert add(7, 3) == 10
    assert add(-2, 2) == 0
    assert add(10, -3) == 7


test_add()


def multiply(a, b):
    return a * b


def test_multiply():
    assert multiply(5, 2) == 10
    assert multiply(3, 0) == 0
    assert multiply(-1, -5) == 5


test_multiply()