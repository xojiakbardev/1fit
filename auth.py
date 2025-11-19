import json
import os
from termcolor import colored
from translation import get_translation as t


def load_data(filename):
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def write_data(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def register_user():
    while True:
        users = load_data("users.json")
        username = input(colored(t("username"), 'magenta'))
        password = input(colored(t("password"), 'magenta'))

        for u in users:
            if u["username"] == username:
                print(colored(t("user_exists"), 'red'))
                break
        else:
            user = {"username": username, "password": password, "role": "user"}
            users.append(user)
            write_data("users.json", users)
            print(colored(t("registration_success"), 'green'))
            return


def login_user():
    while True:
        users = load_data("users.json")
        username = input(colored(t("username"), 'magenta'))
        password = input(colored(t("password"), 'magenta'))

        for u in users:
            if u["username"] == username and u["password"] == password:
                print(colored(f"🟢 {t('welcome')} {username}!", 'green'))
                return u

        print(colored(t("invalid_login"), 'red'))


def create_superuser():
    users = load_data("users.json")
    for u in users:
        if u["role"] == "superuser":
            return 

    print(colored("▶ Superuser creation", "green"))
    username = input(colored(t("username"), 'magenta'))
    password = input(colored(t("password"), 'magenta'))

    superuser = {"username": username,
                 "password": password, "role": "superuser"}
    users.append(superuser)
    write_data("users.json", users)
    print(colored("Superuser created!", "green"))


def create_admin():
    admins = load_data("admins.json")
    username = input(colored(t("username"), 'magenta'))
    password = input(colored(t("password"), 'magenta'))

    admin = {"username": username, "password": password}
    admins.append(admin)
    write_data("admins.json", admins)
    print(colored(t("create_admin"), 'green'))


def superuser_menu():
    while True:
        print(colored("\n--- SUPERUSER MENU ---", 'green'))
        print("1. " + t("create_admin"))
        print("2. " + t("logout"))

        cmd = input(colored(t("choice"), 'magenta'))

        if cmd == "1":
            create_admin()
        elif cmd == "2":
            break
        else:
            print(colored(t("invalid_choice"), 'red'))
