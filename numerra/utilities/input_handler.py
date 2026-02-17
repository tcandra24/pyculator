from numerra.core.errors import InvalidInputError, InvalidMenuError
from numerra.enums.menu import Menu

def input_menu():
  value = input_validation(input("Enter a menu : "))
  if value is None:
    raise InvalidInputError("Menu harus dalam bentuk angka")

  try:
    return Menu(value)
  except ValueError:
    raise InvalidMenuError("Menu Tidak Ada")
    

def input_validation(value):
  try:
    return int(value)
  except ValueError:
    return None

def loop_validation_input(message):
  result = None
  while True:
    result = input_validation(input(message))
    if result is not None: 
      break
    else:
      print("Inputan Salah, Silahkan Coba Lagi!!")

  return result
    
