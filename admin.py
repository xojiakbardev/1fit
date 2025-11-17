from termcolor import colored
import os

from menus import *

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def control_club():
    


def main():
    print(colored("""
╔══════════════════════════════════╗
║          ADMIN PANEL             ║
╚══════════════════════════════════╝
    """, "green", attrs=["bold"]))
    # admin kirish qismi bo'ladi va kirgandan keyin true qaytsa davom etadi
    # if login_admin()
    choice = get_admin_menu()
    match choice:
        case '1':
            print('klublar boshqaruvi')
        case '2':
            print("Mashg‘ulotlar boshqaruvi")
        case '3':
            print('Foydalanuvchilar bo‘limi')
        case '4':
            print("Statistika")
        case '5':
            print('chiqish')
        case _:
            print()
       
main()
