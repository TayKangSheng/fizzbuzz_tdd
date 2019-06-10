import fizzbuzz
import pytest

def test_return_itself():
    assert fizzbuzz.fizzbuzz(1) == 1
    assert fizzbuzz.fizzbuzz(2) == 2

def test_return_fizz_for_multiple_of_three():
    assert fizzbuzz.fizzbuzz(3) == "Fizz"
    assert fizzbuzz.fizzbuzz(6) == "Fizz"

def test_return_buzz_for_multiple_of_five():
    assert fizzbuzz.fizzbuzz(5) == "Buzz"
    assert fizzbuzz.fizzbuzz(10) == "Buzz"

def test_return_fizzbuzz_for_multiple_of_three_and_five():
    assert fizzbuzz.fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz.fizzbuzz(30) == "FizzBuzz"

def test_raise_value_error_for_out_of_range():
    with pytest.raises(ValueError):
        fizzbuzz.fizzbuzz(-1)

    with pytest.raises(ValueError):
        fizzbuzz.fizzbuzz(101)
