from user import user_menu
from admin import admin_menu
from termcolor import colored
from superuser import superuser_menu
from utils import clear_console, draw_box


def main_menu():
    while True:
        draw_box("SPORT KLUBI TIZIMI", "cyan")
        print(colored("\n1. Foydalanuvchi", "yellow"))
        print(colored("2. Admin", "yellow"))
        print(colored("3. Chiqish", "red"))
        print(colored("0. Superuser (yashirin)", "magenta"))

        choice = input(colored("\nTanlang: ", "green"))

        match choice:
            case "1":
                clear_console()
                user_menu()
            case "2":
                clear_console()
                admin_menu()
            case "3":
                clear_console()
                print(colored("\n✅ Xayr!", "green"))
                break
            case "0":
                clear_console()
                superuser_menu()


if __name__ == "__main__":
    main_menu()
