from termcolor import colored
from utils import clear_console
from storage import get_data, save_data, get_new_id

USER_FILE = "data/users.json"
CLUB_FILE = "data/clubs.json"
PAYMENT_FILE = "data/payments.json"


def admin_menu():
    clear_console()
    print(colored("\n🔐 ADMIN KIRISH\n", "green", attrs=["bold"]))
    login = input(colored("Login: ", "cyan"))
    password = input(colored("Parol: ", "cyan"))

    users = get_data(USER_FILE)
    admin = None
    for user in users:
        if user['login'] == login and user['password'] == password and user.get('role') == 'admin':
            admin = user
            break

    if not admin:
        clear_console()
        print(colored("❌ Login yoki parol xato!", "red"))
        return

    while True:
        print(
            colored(f"\n=== ADMIN PANEL ({admin['full_name']}) ===\n", "green", attrs=["bold"]))
        print("1. Statistika")
        print("2. Foydalanuvchilar")
        print("3. Klublar")
        print("4. Orqaga")

        choice = input(colored("\nTanlang: ", "green"))

        match choice:
            case "1":
                clear_console()
                statistic()
            case "2":
                clear_console()
                get_users()
            case "3":
                clear_console()
                club_menu()
            case "4":
                break


def statistic():
    from datetime import datetime

    users = get_data(USER_FILE)
    payments = get_data(PAYMENT_FILE)
    clubs = get_data(CLUB_FILE)

    users = [u for u in users if u.get('role') == 'user']
    now_month = datetime.now().month
    month_users = [u for u in users if u.get('month') == now_month]

    reja_1 = len([p for p in payments if p.get('plan') == 1])
    reja_3 = len([p for p in payments if p.get('plan') == 3])
    reja_6 = len([p for p in payments if p.get('plan') == 6])

    total = sum([p.get('payment', 0) for p in payments])

    print(colored("\n📊 STATISTIKA", "cyan", attrs=["bold"]))
    print(f"Jami foydalanuvchilar: {len(users)}")
    print(f"Bu oy ro'yxatdan o'tganlar: {len(month_users)}")
    print(f"Oylik foyda: {total} so'm")
    print(f"1 oylik: {reja_1}, 3 oylik: {reja_3}, 6 oylik: {reja_6}")
    print(f"Klublar soni: {len(clubs)}")


def get_users():
    users = get_data(USER_FILE)
    userlar = [u for u in users if u.get('role') == 'user']

    if not userlar:
        print(colored("\n📋 Foydalanuvchilar yo'q", "yellow"))
        return

    print(colored("\n=== FOYDALANUVCHILAR ===", "cyan"))
    for u in userlar:
        print(
            f"{u['id']}. {u['full_name']} - {u.get('city', 'N/A')}, {u.get('region', 'N/A')}")


def club_menu():
    while True:
        print(colored("\n=== KLUBLAR BOSHQARUVI ===", "yellow"))
        print(colored("1. Klublar ro'yxati", "green"))
        print(colored("2. Klub qo'shish", "green"))
        print(colored("3. Klub o'chirish", "red"))
        print(colored("4. Orqaga", "yellow"))

        tanlov = input(colored("\nTanlang: ", "green"))

        if tanlov == "1":
            clear_console()
            clubs_list()
        elif tanlov == "2":
            clear_console()
            add_club()
        elif tanlov == "3":
            clear_console()
            delete_club()
        elif tanlov == "4":
            break


def clubs_list():
    clubs = get_data(CLUB_FILE)

    if not clubs:
        print(colored("\n📋 Klublar yo'q", "yellow"))
        return

    print(colored("\n=== KLUBLAR ===", "cyan"))
    for c in clubs:
        print(f"{c['id']}. {c['name']} - {c['city']}, {c['region']} ({c['category']})")


def add_club():
    clubs = get_data(CLUB_FILE)

    club_name = input(colored("\nKlub nomi: ", "cyan"))
    city = input(colored("Shahar: ", "cyan"))
    region = input(colored("Tuman: ", "cyan"))

    print(colored("\nKategoriya:\n", "yellow"))
    print(colored("1. Suzish zal", "green"))
    print(colored("2. Trenajyor", "green"))
    print(colored("3. Ot minish\n", "green"))

    category_choice = input(colored("Tanlang: ", "green"))
    category = {
        "1": "suzish",
        "2": "trenajyor",
        "3": "ot_minish"
    }.get(category_choice, "trenajyor")

    new_club = {
        'id': get_new_id(clubs),
        'name': club_name,
        'city': city,
        'region': region,
        'category': category
    }

    clubs.append(new_club)
    save_data(CLUB_FILE, clubs)
    print(colored("✅ Klub qo'shildi!", "green"))


def delete_club():
    clubs = get_data(CLUB_FILE)

    if not clubs:
        clear_console()
        print(colored("\n❌ Klublar yo'q", "red"))
        return

    clubs_list()
    club_id = int(input(colored("\nO'chirish uchun ID: ", "red")))

    clubs = [c for c in clubs if c['id'] != club_id]
    save_data(CLUB_FILE, clubs)
    print(colored("✅ Klub o'chirildi!", "green"))
