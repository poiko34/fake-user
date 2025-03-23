import random
import faker
from faker.providers import credit_card

# Создаем объект faker
fake = faker.Faker('ru_RU')

# Подключаем провайдер для генерации номеров кредитных карт
fake.add_provider(credit_card)

# Список возможных профессий
professions = ["Программист", "Дизайнер", "Менеджер", "Маркетолог", "Аналитик", "Учитель", "Врач", "Инженер"]

# Список возможных интересов
interests = ["Спорт", "Музыка", "Путешествия", "Чтение", "Технологии", "Игры", "Кулинария", "Фотография"]

# Список любимых блюд
favorite_foods = ["Пицца", "Суши", "Паста", "Бургер", "Салат", "Торт", "Суп"]

# Список любимых фильмов
favorite_movies = ["Интерстеллар", "Матрица", "Гарри Поттер", "Титаник", "Начало"]

# Список типов семейных отношений
family_relations = ["Хорошие отношения с родителями", "Редко общаются с семьей", "Семья далеко", "Не общаются с семьей"]

# Список желаемых целей/мечт
dreams = ["Путешествовать по миру", "Открыть свой бизнес", "Становиться лучше в своей профессии", "Написать книгу"]

# Список уровней дохода
income_levels = ["Низкий", "Средний", "Высокий", "Очень высокий"]

# Список типов личности
personality_types = ["Экстраверт", "Интроверт"]

# Список уровней образования
education_levels = ["Высшее", "Среднее", "Начальное"]

# Список возможных мест выдачи паспорта
passport_issuers = ["Отдел МВД России", "Государственный центр", "ФМС", "УФМС"]

# Функция генерации случайной личности
def generate_extended_fake_personality():
    name = fake.name()  # Генерация случайного имени
    age = random.randint(18, 60)  # Случайный возраст
    gender = random.choice(["Мужчина", "Женщина", "Другой"])  # Случайный пол
    profession = random.choice(professions)  # Случайная профессия
    interest = random.choice(interests)  # Случайный интерес
    city = fake.city()  # Случайный город
    marital_status = random.choice(["Женат/замужем", "Холост/незамужняя", "В разводе", "Вдова/вдовец"])  # Состояние в браке
    children = random.choice(["Есть дети", "Нет детей"])  # Есть ли дети
    education = random.choice(education_levels)  # Уровень образования
    personality_type = random.choice(personality_types)  # Тип личности
    income = random.choice(income_levels)  # Уровень дохода
    hobbies = random.sample(interests, 2)  # Два случайных хобби
    birthdate = fake.date_of_birth(minimum_age=18, maximum_age=60)  # Генерация даты рождения
    phone_number = fake.phone_number()  # Генерация номера телефона
    favorite_food = random.choice(favorite_foods)  # Любимая еда
    favorite_movie = random.choice(favorite_movies)  # Любимый фильм
    family_relation = random.choice(family_relations)  # Семейные отношения
    dream = random.choice(dreams)  # Желания/мечты

    # Генерация случайных номеров карт (например, для кредиток)
    credit_card_number = fake.credit_card_number(card_type="mastercard")  # Генерация Mastercard
    credit_card_expiry = fake.credit_card_expire()  # Генерация срока действия карты
    credit_card_provider = fake.credit_card_provider()  # Генерация провайдера карты (например, "MasterCard")

    # Генерация CVC кода (для MasterCard 3 цифры, для American Express 4)
    cvc_code = random.randint(100, 999)  # Генерация 3-значного CVC для большинства карт
    if credit_card_provider.lower() == "american express":
        cvc_code = random.randint(1000, 9999)  # Для American Express 4-значный CVC

    # Генерация паспортных данных
    passport_series = f"{random.randint(10, 99)}"  # Серия паспорта (2 цифры)
    passport_number = f"{random.randint(100000, 999999)}"  # Номер паспорта (6 цифр)
    passport_issue_date = fake.date_this_century()  # Дата выдачи
    passport_issuer = random.choice(passport_issuers)  # Место выдачи
    passport_code = f"{random.randint(1000, 9999)}"  # Код подразделения
    passport_firstname = name.split()[1]  # Имя из полного имени
    passport_lastname = name.split()[0]  # Фамилия из полного имени
    passport_patronymic = fake.first_name_male()  # Отчество (для мужчин, например)
    passport_birthdate = birthdate  # Дата рождения
    passport_gender = gender  # Пол
    passport_nationality = "Россия"  # Гражданство
    passport_address = fake.address()  # Адрес регистрации
    passport_signature = "Подпись владельца паспорта"  # Символическая подпись
    passport_photo = "Фото владельца паспорта"  # Символическое фото

    # Формирование полной личности
    extended_personality = {
        "Основная информация": {
            "Имя": name,
            "Возраст": age,
            "Пол": gender,
            "Профессия": profession,
            "Интерес": interest,
            "Город": city,
            "Семейное положение": marital_status,
            "Дети": children,
            "Образование": education,
            "Тип личности": personality_type,
            "Уровень дохода": income,
            "Хобби": hobbies,
            "Дата рождения": birthdate
        },
        "Кредитные карты": {
            "Номер карты": credit_card_number,
            "Срок действия карты": credit_card_expiry,
            "CVC код": cvc_code,
            "Провайдер карты": credit_card_provider

        },
        "Паспортные данные": {
            "Серия паспорта": passport_series,
            "Номер паспорта": passport_number,
            "Дата выдачи паспорта": passport_issue_date,
            "Место выдачи паспорта": passport_issuer,
            "Код подразделения": passport_code,
            "Имя": passport_firstname,
            "Фамилия": passport_lastname,
            "Отчество": passport_patronymic,
            "Дата рождения паспорта": passport_birthdate,
            "Пол паспорта": passport_gender,
            "Гражданство": passport_nationality,
            "Адрес регистрации": passport_address,
            "Подпись владельца паспорта": passport_signature,
            "Фото владельца паспорта": passport_photo
        },
        "Контактная информация": {
            "Телефон": phone_number,
            "Адрес": fake.address()  # Генерация случайного адреса
        },
        "Интересы и хобби": {
            "Любимая еда": favorite_food,
            "Любимый фильм": favorite_movie,
            "Семейные отношения": family_relation,
            "Мечта": dream
        }
    }

    return extended_personality

# Генерация и вывод расширенной личности
extended_fake_personality = generate_extended_fake_personality()

# Выводим результат с сортировкой
for section, data in extended_fake_personality.items():
    print(f"\n{section}:")
    # Сортируем ключи внутри раздела
    for key, value in sorted(data.items()):
        print(f"  {key}: {value}")
