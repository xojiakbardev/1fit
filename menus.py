from termcolor import colored
import os
from translation import *


def clear(): os.system('cls' if os.name == 'nt' else 'clear')


def banner():
    print(colored("""
╔══════════════════════════════════╗
║         💪 ONEFIT 💪      ║
╚══════════════════════════════════╝
    """, "green", attrs=["bold"]))

def main_menu():
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


def get_admin_menu():
    box = f"""
+----------------+
|     Menu       |
+----------------+
"""
    print(colored("""1️⃣. Klublar boshqaruvi
2️⃣. Mashg'ulotlar boshqaruvi
3️⃣. Foydalanuvchilar
4️⃣. Statiska
5️⃣. Chiqish""", 'yellow'))
    choice = input(colored(get_translation("choice"), "magenta"))
    return choice

def club_management_menu():
    box = f"""
+--------------------------+
|     Klub boshqaruvi      |
+--------------------------+
"""
    print(colored(box, 'green'))
    print(colored("""1️⃣. Klublar ro'yhati
2️⃣. Yangi klub qo'shish
3️⃣. Klub o'chirish
4️⃣. Klub ma'lumotlarini tahrirlash
5️⃣. Statiska
6️⃣. Chiqish""", 'yellow'))
    choice = input(colored(get_translation("choice"), "magenta"))
    return choice
    

def training_management_menu():
    box = f"""
+-----------------------------------+
|     Mashg'ulotlar boshqaruvi      |
+-----------------------------------+
"""
    print(colored(box, 'green'))
    print(colored("""1️⃣. Yangi mashg'ulot qo'shish
2️⃣. Mashg'ulot o'chirish
3️⃣. Ortga qaytish
""", 'yellow'))
    choice = input(colored(get_translation("choice"), "magenta"))
    return choice
    
    
