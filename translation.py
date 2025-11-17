# translations.py

translations = {
    "en": {
        "welcome": "Welcome to ONE FIT SYSTEM!",
        "register": "Register",
        "login": "Login",
        "exit": "Exit",
        "choice": "Your choice: ",
        "invalid_choice": "Invalid choice!",
        "goodbye": "Goodbye!",
        "username": "Username: ",
        "password": "Password: ",
        "age": "Age: ",
        "weight": "Weight (kg): ",
        "height": "Height (cm): ",
        "invalid_input": "Invalid input!",
        "user_exists": "User already exists!",
        "registration_success": "Registration successful!",
        "invalid_login": "Invalid username or password!",
        "error": "Error",
    },
    "uz": {
        "welcome": "ONE FIT SYSTEMga xush kelibsiz!",
        "register": "Ro‘yxatdan o‘tish",
        "login": "Tizimga kirish",
        "exit": "Chiqish",
        "choice": "Tanlovingiz: ",
        "invalid_choice": "Noto‘g‘ri tanlov!",
        "goodbye": "Xayr!",
        "username": "Foydalanuvchi nomi: ",
        "password": "Parol: ",
        "age": "Yosh: ",
        "weight": "Vazn (kg): ",
        "height": "Bo‘y (cm): ",
        "invalid_input": "Noto‘g‘ri ma'lumot kiritildi!",
        "user_exists": "Bu foydalanuvchi allaqachon mavjud!",
        "registration_success": "Ro‘yxatdan muvaffaqiyatli o‘tdingiz!",
        "invalid_login": "Noto‘g‘ri login yoki parol!",
        "error": "Xatolik",
    },
    "ru": {
        "welcome": "Добро пожаловать в ONE FIT SYSTEM!",
        "register": "Регистрация",
        "login": "Войти",
        "exit": "Выход",
        "choice": "Ваш выбор: ",
        "invalid_choice": "Неверный выбор!",
        "goodbye": "До свидания!",
        "username": "Имя пользователя: ",
        "password": "Пароль: ",
        "age": "Возраст: ",
        "weight": "Вес (кг): ",
        "height": "Рост (см): ",
        "invalid_input": "Неверный ввод!",
        "user_exists": "Пользователь уже существует!",
        "registration_success": "Регистрация успешна!",
        "invalid_login": "Неверное имя пользователя или пароль!",
        "error": "Ошибка",
    }
}

selected_language = "en"


def get_translation(key):
    return translations[selected_language].get(key, str(key))


def set_language(language):
    global selected_language
    selected_language = language
