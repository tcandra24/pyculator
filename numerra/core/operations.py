from numerra.core.errors import InvalidMenuError, DivisionByZeroError
from numerra.core.calculator import Calculator
from numerra.core.history import HistoryItem
from numerra.enums.menu import Menu

OPERATIONS = {
  Menu.ADD: { "symbol": "+", "func": Calculator.add},
  Menu.SUB: { "symbol": "-", "func": Calculator.sub},
  Menu.MUL: { "symbol": "*", "func": Calculator.multiply},
  Menu.DIV: { "symbol": "/", "func": Calculator.division}
}

def execute_operation(menu, value_1, value_2, histories):
  operation = OPERATIONS.get(menu)
  if not operation:
    raise InvalidMenuError("Operasi tidak tersedia")

  if operation["symbol"] == "/" and value_2 == 0:
    raise DivisionByZeroError("Tidak Bisa Dibagi dengan 0")

  result = operation["func"](value_1, value_2)
  histories.add_history(HistoryItem(value_1, value_2, operation["symbol"], result))

  return result