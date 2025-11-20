from datetime import datetime
import time
from termcolor import colored
from storage import get_data, save_data, get_new_id

from utils import clear_console, draw_box, show_progres

USER_FILE = "data/users.json"
CLUB_FILE = "data/clubs.json"
PAYMENT_FILE = "data/payments.json"


def user_menu():
    print(colored("\n👤 FOYDALANUVCHI\n", "blue", attrs=["bold"]))
    print(colored("1. Ro'yxatdan o'tish", 'yellow'))
    print(colored("2. Kirish", 'yellow'))
    print(colored("3. Orqaga", 'yellow'))

    choice = input(colored("\nTanlang: ", "green"))

    match choice:
        case "1":
            clear_console()
            register_user()
        case "2":
            clear_console()
            login_user()
        case "3":
            return


def register_user():
    draw_box("FOYDALANUVCHI RO'YXATDAN OTISH")
    users = get_data(USER_FILE)

    full_name = input(colored("\nTo'liq Ism: ", "yellow"))
    login = input(colored("Login: ", "yellow"))
    parol = input(colored("Parol: ", "yellow"))
    shahar = input(colored("Shahar: ", "yellow"))
    tuman = input(colored("Tuman: ", "yellow"))

    if any(uuser['login'] == login for uuser in users):
        clear_console()
        print(colored("❌ Bu login band!", "red"))
        return

    new_user = {
        'id': get_new_id(users),
        'full_name': full_name,
        'login': login,
        'password': parol,
        'city': shahar,
        'region': tuman,
        'role': 'user',
        'month': datetime.now().month,
        'year': datetime.now().year,
        'day': datetime.now().day
    }

    users.append(new_user)
    show_progres("Foydalanuvchi yaratilmoqda...")
    save_data(USER_FILE, users)
    print(colored("\n✅ Ro'yxatdan o'tdingiz!", "green"))
    time.sleep(1)
    user_panel(new_user)


def login_user():
    draw_box("FOYDALANUVCHI KIRISH")
    login = input(colored("\nLogin: ", "yellow"))
    parol = input(colored("Parol: ", "yellow"))

    users = get_data(USER_FILE)
    user = None
    for u in users:
        if u['login'] == login and u['password'] == parol:
            user = u
            break

    if not user:
        clear_console()
        print(colored("❌ Login yoki parol xato!", "red"))
        return
    show_progres("Tizimga kirilmoqda...")
    user_panel(user)


def user_panel(user):
    clear_console()
    while True:
        print(
            colored(f"\n=== {user['full_name']} ===", "blue", attrs=["bold"]))
        print(colored("1. Barcha klublar", "green"))
        print(colored("2. Tavsiya qilingan klublar", "green"))
        print(colored("3. Klublarga obuna bo'lish", "green"))
        print(colored("4. Orqaga", "yellow"))

        choice = input(colored("\nTanlang: ", "green"))

        match choice:
            case "1":
                clear_console()
                clubs()
            case "2":
                clear_console()
                recommended_clubs(user)
            case "3":
                clear_console()
                subscribe(user)
            case "4":
                break


def clubs():
    clubs = get_data(CLUB_FILE)

    if not clubs:
        print(colored("\n📋 Klublar yo'q", "yellow"))
        return

    print(colored("\n=== BARCHA KLUBLAR ===", "cyan"))
    for c in clubs:
        print(
            f"{c['id']}. {c['name']} - {c['city']}, {c['region']} ({c['category']})")


def recommended_clubs(user):
    clubs = get_data(CLUB_FILE)

    tavsiya = [c for c in clubs if c['city'] ==
               user['city'] and c['region'] == user['region']]

    if not tavsiya:
        print(
            colored(f"\n📋 {user['city']}, {user['region']} uchun klublar yo'q", "yellow"))
        return

    print(colored(
        f"\n⭐ TAVSIYA ETILGAN KLUBLAR ({user['city']}, {user['region']})", "green", attrs=["bold"]))
    for c in tavsiya:
        print(f"{c['id']}. {c['name']} ({c['category']})")


def subscribe(user):
    clubs = get_data(CLUB_FILE)
    payments = get_data(PAYMENT_FILE)

    if not clubs:
        clear_console()
        print(colored("\n❌ Klublar yo'q", "red"))
        return

    print(colored("\n=== KLUBLAR ===", "cyan"))
    for c in clubs:
        print(f"{c['id']}. {c['name']}")

    club_id = int(input(colored("\nKlub ID: ", "green")))
    club = None
    for c in clubs:
        if c['id'] == club_id:
            club = c
    if any(p['user_id'] == user['id'] and p['club_id'] == club_id for p in payments):
        clear_console()
        print(colored("\n❌ Bu klubga avval obuna bo'lgansiz!", "red"))
        return

    if not club:
        clear_console()
        print(colored("❌ Klub topilmadi!", "red"))
        return

    print(colored("\n=== OBUNA REJASI ===", "yellow"))
    print(colored("1. 1 oy - 300,000 so'm", "green"))
    print(colored("2. 3 oy - 850,000 so'm (chegirma 5%)", "green"))
    print(colored("3. 6 oy - 1,600,000 so'm (chegirma 10%)", "green"))

    plans = int(input(colored("\nTanlang: ", "green")))
    credit_card = input(colored("Karta raqami: ", "green"))
    phone = input(colored("Telefon raqami: ", "green"))

    prices = {1: 300000, 2: 850000, 3: 1600000}
    discounts = {1: 0, 2: 5, 3: 10}

    oy = {1: 1, 2: 3, 3: 6}.get(plans, 1)
    price = prices.get(plans, 300000)
    discount = discounts.get(plans, 0)
    payment = int(price * (1 - discount / 100))

    new_payment = {
        'id': get_new_id(payments),
        'user_id': user['id'],
        'club_id': club_id,
        'plan': oy,
        'price': price,
        'discount': discount,
        'payment': payment,
        'credit_card': credit_card,
        'phone': phone
    }

    payments.append(new_payment)
    save_data(PAYMENT_FILE, payments)

    print(colored(f"\n✅ Obuna sotib olindi!", "green"))
    print(colored(f"Klub: {club['name']}", "cyan"))
    print(colored(f"Muddat: {oy} oy", "cyan"))
    print(colored(f"Narx: {price} so'm", "yellow"))
    print(colored(f"Chegirma: {discount}%", "yellow"))
    print(colored(f"To'lov: {payment} so'm", "green", attrs=["bold"]))
