import json
import os


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
    users = load_data("users.json")
    username = input("Username kiriting: ")
    password = input("Parol kiriting: ")

    for u in users:
        if u["username"] == username:
            print("Bu username band!")
            return

    user = {"username": username, "password": password, "role": "user"}
    users.append(user)
    write_data("users.json", users)
    print("Ro'yxatdan o'tdingiz!")


def login():
    users = load_data("users.json")
    username = input("Username: ")
    password = input("Parol: ")

    for u in users:
        if u["username"] == username and u["password"] == password:
            print("Xush kelibsiz,", username)
            return u

    print("Login yoki parol xato!")
    return None


def create_superuser():
    users = load_data("users.json")
    for u in users:
        if u["role"] == "superuser":
            return

    print("Superuser yaratish:")
    username = input("Superuser username: ")
    password = input("Parol: ")

    superuser = {"username": username,
                 "password": password, "role": "superuser"}
    users.append(superuser)
    write_data("users.json", users)
    print("Superuser yaratildi!")


def create_admin():
    admins = load_data("admins.json")
    username = input("Admin username: ")
    password = input("Parol: ")

    admin = {"username": username, "password": password}
    admins.append(admin)
    write_data("admins.json", admins)
    print("Admin yaratildi!")


def superuser_menu():
    while True:
        print("\n--- SUPERUSER MENU ---")
        print("1. Admin yaratish")
        print("2. Chiqish")
        cmd = input("Tanlang: ")

        if cmd == "1":
            create_admin()
        elif cmd == "2":
            break
        else:
            print("Noto'g'ri buyruq!")


def main():
    create_superuser()

    while True:
        print("\n--- ONEFIT AUTHSYS ---")
        print("1. Ro'yxatdan o'tish")
        print("2. Login")
        print("3. Chiqish")

        cmd = input("Tanlang: ")

        if cmd == "1":
            register_user()
        elif cmd == "2":
            user = login()
            if user:
                if user["role"] == "superuser":
                    superuser_menu()
                else:
                    print("Oddiy user sifatida kirdingiz.")
        elif cmd == "3":
            print("Dastur tugadi.")
            break
        else:
            print("Xato buyruq!")


main()
