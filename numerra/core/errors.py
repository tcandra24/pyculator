class CalculatorError(Exception):
  pass

class InvalidMenuError(CalculatorError):
  pass

class InvalidInputError(CalculatorError):
  pass

class DivisionByZeroError(CalculatorError):
  pass