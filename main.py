import os
from termcolor import colored

from translation import *
from menus import *


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def banner():
    print(colored("""
╔══════════════════════════════════╗
║         💪 ONEFIT 💪      ║
╚══════════════════════════════════╝
    """, "green", attrs=["bold"]))

def main():
    clear()
    banner()

    user_data = None
    language_choice = print_select_language()
    if language_choice == '1':
        set_language('en')
    elif language_choice == '2':
        set_language('uz')
    elif language_choice == '3':
        set_language('ru')
    else:
        print("Invalid choice, defaulting to English.")
        set_language('en')

    match language_choice:
        case '1':
            set_language('en')
        case '2':
            set_language('uz')
        case '3':
            set_language('ru')
        case _:
            print("Invalid choice, defaulting to English.")
            set_language('en')


    
    while True:
        if not user_data:
            clear()
            choice = menu1()

            match choice:
                case '1':
                    print('register')
                case '2':
                    print('login')
                case '3':
                    print(colored(get_translation("goodbye"), "red"))
                    return
                case _:
                    print(colored(get_translation("invalid_choice"), "red"))
        else:
            clear()


            
main()



