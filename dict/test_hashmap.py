from hashmap import *


def test_take_while():
    expected = [1, 2, 3, 4, 5]
    actual = list(
        take_while(gt(6), range(1, 10))
    )
    assert actual == expected


def test_smaller_unsigned_integer_that_fits_n():
    expected = "uint32"
    actual = smaller_unsigned_integer_that_fits_(100_000)
    assert actual == expected


def test_take_one_above():
    expected = 6
    actual = take_one_above(gt(6), range(1, 10))
    assert actual == expected