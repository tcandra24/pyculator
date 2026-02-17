from numerra.core.calculator import Calculator
from numerra.core.errors import DivisionByZeroError

from pytest import raises

def test_addition():
  assert Calculator.add(2, 3) == 5

def test_subtraction():
  assert Calculator.sub(5, 10) == -5

def test_multiplication():
  assert Calculator.multiply(10, 2) == 20

def test_division():
  assert Calculator.division(10, 2) == 5

def test_division_by_zero():
  with raises(DivisionByZeroError):
    Calculator.division(10, 0)


