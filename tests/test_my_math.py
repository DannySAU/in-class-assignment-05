import pytest

from src.my_math import sum, multiply, difference, absolute_sum,calculate_birth_year

def test_sum():
    res = sum(1,1)
    assert res == 2

# Work together
def test_multiply():
    res = multiply(2,2)
    assert res == 4


# Check for understanding
## Test difference

def test_difference():
    res = difference(5,1)
    assert res == 4

# Work together
## Test absolute sum

def test_it_should_be_positive_lol():
    res = absolute_sum(1,3)
    assert res == 4
def test_should_be_positive_dos():
    res=absolute_sum(-19,-14)
    assert res == 33

# Check for understanding
## Test calculate age

def test_calculate_age_LOL():
    res = calculate_birth_year(2040, 80, False)
    assert res == 1959

def test_calculate_if_nah():
    res = calculate_birth_year(2020, 60, True)
    assert res == 1960