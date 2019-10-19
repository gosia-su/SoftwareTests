import my_math


def test_add():
    assert my_math.add(7, 3) == 10
    assert my_math.add(-2, 2) == 0
    assert my_math.add(10, -3) == 7


# test_add()


def test_multiply():
    assert my_math.multiply(5, 2) == 10
    assert my_math.multiply(3, 0) == 0
    assert my_math.multiply(-1, -5) == 5


# test_multiply()


def test_reversed():
    assert my_math.reversed('home') == 'emoh'
    assert my_math.reversed('ABcd') == 'dcBA'
    assert my_math.reversed('nuda') == 'adnn'

#
# test_reversed()

# snakecase => dla nazw plikow i funkcji => to_jest_nazwa
# CamelCase => dla nazw klas => To_Jest_Nazwa