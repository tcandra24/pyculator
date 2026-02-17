from numerra.core.errors import DivisionByZeroError

class Calculator:
  @staticmethod
  def add(a, b):
    return a + b

  @staticmethod
  def sub(a, b):
    return a - b

  @staticmethod
  def multiply(a, b):
    return a * b

  @staticmethod
  def division(a, b):
    if b ==0 :
      raise DivisionByZeroError
    return a / b