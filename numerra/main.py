import argparse

from numerra.utilities.input_handler import input_menu, loop_validation_input
from numerra.core.operations import execute_operation
from numerra.core.errors import CalculatorError
from numerra.core.history import History
from numerra.enums.menu import Menu
from numerra.logs.logging import logging
from numerra.config.config import load_config

def menu_mode(histories):

    while True:
        print ("""
Choose Menu:
1. Penjumlahan
2. Pengurangan
3. Perkalian
4. Pembagian
5. History
6. Hapus History
7. Keluar
        """)
        menu = input_menu()

        if menu == Menu.EXIT: 
            print("Terima Kasih!!")
            break

        if menu == Menu.HISTORY:
            histories.show()
            continue

        if menu == Menu.CLEAR:
            histories.clear()
            print("History berhasil dihapus!")
            continue
        
        value_1 = loop_validation_input("Masukan Angka Pertama : ")
        value_2 = loop_validation_input("Masukan Angka Kedua : ")

        result = execute_operation(menu, value_1, value_2, histories)
        print(f"Hasilnya yaitu : {result}")        

def interactive_mode(args, parser, histories):
    if args.add:
        menu = Menu.ADD
    elif args.sub:
        menu = Menu.SUB
    elif args.multiply:
        menu = Menu.MUL
    elif args.division:
        menu = Menu.DIV
    elif args.histories:
        histories.show()
        return
    elif args.clear:
        histories.clear()
        print("History berhasil dihapus!")
        return
    else: 
        parser.print_help()
        return

    value_1 = args.value1 if args.value1 is not None else loop_validation_input("Masukan Angka Pertama : ")
    value_2 = args.value2 if args.value2 is not None else loop_validation_input("Masukan Angka Kedua : ")

    result = execute_operation(menu, value_1, value_2, histories)
    print(f"Hasilnya yaitu : {result}")
        
def main():
    parser = argparse.ArgumentParser(description="Python Calculator Project")
    parser.add_argument("--version", action="version", version="Python Calculator Project 0.1.4")
    parser.add_argument("--menu", action="store_true", help="Menu Mode for Calculator")

    parser.add_argument("-a", "--add", action="store_true", help="Choose add mode for Calculator")
    parser.add_argument("-s", "--sub", action="store_true", help="Choose sub mode for Calculator")
    parser.add_argument("-m", "--multiply", action="store_true", help="Choose multiply mode for Calculator")
    parser.add_argument("-d", "--division", action="store_true", help="Choose division mode for Calculator")

    parser.add_argument("--histories", action="store_true", help="Show Calculator Histories")
    parser.add_argument("--clear", action="store_true", help="Clear Calculator Histories")

    parser.add_argument("value1", type=int, nargs="?", help="First value for calculation")
    parser.add_argument("value2", type=int, nargs="?", help="Second value for calculation")

    args = parser.parse_args()

    config = load_config()

    histories = History(config.max_history, config.auto_save)
    
    try:
        if args.menu:
            menu_mode(histories)
        else:
            interactive_mode(args, parser, histories)
    except CalculatorError as e:
        logging(f"Error : {e}")
        print(f"Error : {e}")

if __name__ == "__main__":
    main()
    