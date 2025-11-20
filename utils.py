import time
import os
from termcolor import colored


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def draw_box(matn, rang="green"):
    kengligi = 60
    chiziq = "─" * kengligi
    print(f"\n{colored(f'┌{chiziq}┐', rang)}")
    print(colored(f"  {matn.center(kengligi)}  ", rang, attrs=["bold"]))
    print(colored(f"└{chiziq}┘", rang))


def show_progres(message):
    for i in range(1, 101):
        time.sleep(0.01)
        bar = '█' * (i // 2)
        print(f"\r [{bar}{' ' * (50 - len(bar))}] {i}% {message}",
              end='', flush=True)
