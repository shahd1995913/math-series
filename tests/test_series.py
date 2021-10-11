from math_series import __version__
from math_series.series import fibonacci
from math_series.series import Lucas

def test_version() :

    assert __version__ == '0.1.0'

def test_Lucas1() :

     assert Lucas(1) == 1

def test_Lucas0() :

    assert Lucas(0) == 2


def test_version1():
    assert fibonacci(input)==1

def test_fibonacci_0():

    assert fibonacci(0)==0

def test_fibonacci_1():

    assert fibonacci(1)==1

def test_fibonacci_N_Number():

    for numbers in range (2,100):

        newFib=fibonacci(numbers-1)+fibonacci(numbers-2)

        assert fibonacci(numbers) == newFib

def test_Lucas_N_numbers() :

    for num in range(2,100):

        numb = Lucas(num-1)+Lucas(num-2)
       
        assert Lucas(num) == numb
