from termcolor import colored
from utils import clear_console, draw_box
from storage import get_data, save_data, get_new_id


SUPER_USER_NAME = "superadmin"
SUPER_USER_PASS = "qwerty"
USER_FILE = "data/users.json"


def superuser_menu():
    clear_console()
    draw_box("SUPERUSER KIRISH")
    username = input(colored("Superuser login: ", "magenta"))
    password = input(colored("Superuser parol: ", "magenta"))
    if username != SUPER_USER_NAME or password != SUPER_USER_PASS:
        print(colored("❌ Xato parol yoki login!", "red"))
        return

    while True:
        print(colored("\n=== SUPERUSER PANEL ===", "magenta", attrs=["bold"]))
        print("1. Adminlar ro'yxati")
        print("2. Admin yaratish")
        print("3. Admin o'chirish")
        print("4. Orqaga")

        choice = input(colored("\nTanlang: ", "green"))

        match choice:
            case "1":
                clear_console()
                admins_list()
            case "2":
                clear_console()
                add_admin()
            case "3":
                clear_console()
                delete_admin()
            case "4":
                break


def admins_list():
    users = get_data(USER_FILE)
    adminlar = [u for u in users if u.get('role') == 'admin']

    if not adminlar:
        print(colored("\n📋 Adminlar yo'q", "yellow"))
        return

    print(colored("\n=== ADMINLAR ===", "cyan"))
    for a in adminlar:
        print(f"{a['id']}. {a['full_name']} - {a['login']}")


def add_admin():
    users = get_data(USER_FILE)

    full_name = input(colored("\nTo'liq Ism: ", "cyan"))
    login = input(colored("Login: ", "cyan"))
    password = input(colored("Parol: ", "cyan"))

    if any(u['login'] == login for u in users):
        print(colored("❌ Bu login band!", "red"))
        return

    new_user = {
        'id': get_new_id(users),
        'full_name': full_name,
        'login': login,
        'password': password,
        'role': 'admin'
    }

    users.append(new_user)
    save_data(USER_FILE, users)
    print(colored("✅ Admin yaratildi!", "green"))


def delete_admin():
    users = get_data(USER_FILE)
    admins = [u for u in users if u.get('role') == 'admin']

    if not admins:
        print(colored("\n❌ Adminlar yo'q", "red"))
        return

    admins_list()
    admin_id = int(input(colored("\nO'chirish uchun ID: ", "red")))

    users = [u for u in users if u['id'] != admin_id]
    save_data(USER_FILE, users)
    print(colored("✅ Admin o'chirildi!", "green"))
