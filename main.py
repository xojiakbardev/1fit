import os
from termcolor import colored

from translation import print_select_language

print(colored("Bold + Underline", "green", attrs=["bold", "underline"]))


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
    print_select_language()



