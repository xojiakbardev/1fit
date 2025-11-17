from termcolor import colored
import os
from translation import *


def clear(): os.system('cls' if os.name == 'nt' else 'clear')



def menu1():
    box = f"""
+------------------------+
|     Kirish usuli       |
+------------------------+
"""
    print(colored(box,'green'))
    print(colored(f"1️⃣  {get_translation('register')}", "yellow"))
    print(colored(f"2️⃣  {get_translation('login')}", "yellow"))
    print(colored(f"3️⃣  {get_translation('exit')}", "yellow"))
    choice = input(colored(get_translation("choice"), "magenta"))
    return choice

menu1()


def get_user_menu():
    clear()
    box = f"""
+----------------+
|     Menu       |
+----------------+
"""

    print(colored(box, 'green', attrs=['blink']))
    print(colored("""1️⃣. Klublar
2️⃣. Mashg'ulotlar
3️⃣. Bronlar
4️⃣. Obuna
5️⃣. Statiska
6️⃣. Chiqish""", 'yellow'))
    choice = input(colored(get_translation("choice"), "magenta"))
    return choice

get_user_menu()

def get_admin_menu():
    box = f"""
+----------------+
|     Menu       |
+----------------+
"""
    print(colored("""1️⃣. Klublar
2️⃣. Klublar boshqaruvi
3️⃣. Mashg'ulotlar boshqaruvi
4️⃣. Foydalanuvchilar
5️⃣. Statiska
6️⃣. Chiqish""", 'yellow'))
    choice = input(colored(get_translation("choice"), "magenta"))
    return choice
