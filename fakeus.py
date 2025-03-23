import random
import faker
from faker.providers import credit_card

# Создаем объект faker
fake = faker.Faker('ru_RU')
fake.add_provider(credit_card)

# Списки для новых данных
professions = ["Программист", "Дизайнер", "Менеджер", "Маркетолог", "Аналитик", "Учитель", "Врач", "Инженер"]
interests = ["Спорт", "Музыка", "Путешествия", "Чтение", "Технологии", "Игры", "Кулинария", "Фотография"]
favorite_foods = ["Пицца", "Суши", "Паста", "Бургер", "Салат", "Торт", "Суп"]
favorite_movies = ["Интерстеллар", "Матрица", "Гарри Поттер", "Титаник", "Начало"]
family_relations = ["Хорошие отношения с родителями", "Редко общаются с семьей", "Семья далеко", "Не общаются с семьей"]
dreams = ["Путешествовать по миру", "Открыть свой бизнес", "Становиться лучше в своей профессии", "Написать книгу"]
income_levels = ["Низкий", "Средний", "Высокий", "Очень высокий"]
personality_types = ["Экстраверт", "Интроверт"]
education_levels = ["Высшее", "Среднее", "Начальное"]
passport_issuers = ["Отдел МВД России", "Государственный центр", "ФМС", "УФМС"]
blood_types = ["I", "II", "III", "IV"]
diseases = ["Нет заболеваний", "Диабет", "Гипертония", "Астма", "Аллергия на пыльцу", "Мигрень"]
vehicles = ["Лада", "Тойота", "Мазда", "Форд", "BMW", "Мерседес", "ВАЗ"]
credit_history = ["Чистая", "Есть задолженность", "Ипотека", "Кредит на автомобиль", "Нет кредитов"]

# Функция для определения пола по имени (условная логика)
def determine_gender(name):
    if name.endswith('а') or name.endswith('я'):
        return "Женщина"
    else:
        return "Мужчина"

# Функция генерации случайной личности
def generate_extended_fake_personality(level=1):
    # Общие данные
    name = fake.name()
    gender = determine_gender(name)  # Определение пола по имени
    age = random.randint(18, 60)
    phone_number = fake.phone_number()

    # Вывод данных в зависимости от уровня генерации
    if level == 1:
        return {
            "Имя": name,
            "Возраст": age,
            "Пол": gender,
            "Телефон": phone_number
        }

    # Дополнительные данные для уровня 2
    if level >= 2:
        # Генерация паспортных данных и кредитной истории
        passport_series = f"{random.randint(10, 99)}"
        passport_number = f"{random.randint(100000, 999999)}"
        passport_issue_date = fake.date_this_century()
        passport_issuer = random.choice(passport_issuers)
        passport_code = f"{random.randint(1000, 9999)}"
        passport_firstname = name.split()[1]
        passport_lastname = name.split()[0]
        passport_patronymic = fake.first_name_male()
        passport_birthdate = fake.date_of_birth(minimum_age=18, maximum_age=60)
        passport_gender = gender
        passport_nationality = "Россия"
        passport_address = fake.address()
        passport_signature = "Подпись владельца паспорта"
        passport_photo = "Фото владельца паспорта"

        # Генерация кредитной истории
        credit_score = random.choice(["Высокий", "Средний", "Низкий"])
        credit_status = random.choice(credit_history)

        extended_personality = {
            "Основная информация": {
                "Имя": name,
                "Возраст": age,
                "Пол": gender,
                "Телефон": phone_number
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
            "Кредитная история": {
                "Кредитный рейтинг": credit_score,
                "Статус кредитной истории": credit_status
            }
        }
        return extended_personality

    # Дополнительные данные для уровня 3
    if level >= 3:
        # Хобби и интересы
        profession = random.choice(professions)
        interest = random.choice(interests)
        favorite_food = random.choice(favorite_foods)
        favorite_movie = random.choice(favorite_movies)
        family_relation = random.choice(family_relations)
        dream = random.choice(dreams)

        # Добавление раздела "Интересы и хобби"
        extended_personality = {
            "Интересы и хобби": {
                "Профессия": profession,
                "Интерес": interest,
                "Любимая еда": favorite_food,
                "Любимый фильм": favorite_movie,
                "Семейные отношения": family_relation,
                "Мечта": dream
            }
        }

        # Добавляем другие данные, если нужно
        if level >= 2:
            extended_personality.update({
                "Основная информация": {
                    "Имя": name,
                    "Возраст": age,
                    "Пол": gender,
                    "Телефон": phone_number
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
                "Кредитная история": {
                    "Кредитный рейтинг": credit_score,
                    "Статус кредитной истории": credit_status
                }
            })

        return extended_personality


# Пример использования
level = int(input("Выберите уровень генерации (1 - базовые данные, 2 - паспортные и кредитные данные, 3 - хобби и интересы): "))
generated_personality = generate_extended_fake_personality(level)

# Вывод данных в зависимости от уровня
print("\nГенерированные данные:")
if level == 1:
    for key, value in generated_personality.items():
        print(f"{key}: {value}")
elif level == 2:
    print("\nОсновная информация:")
    for key, value in generated_personality["Основная информация"].items():
        print(f"{key}: {value}")
    print("\nПаспортные данные:")
    for key, value in generated_personality["Паспортные данные"].items():
        print(f"{key}: {value}")
    print("\nКредитная история:")
    for key, value in generated_personality["Кредитная история"].items():
        print(f"{key}: {value}")
elif level == 3:
    print("\nОсновная информация:")
    for key, value in generated_personality["Основная информация"].items():
        print(f"{key}: {value}")
    print("\nПаспортные данные:")
    for key, value in generated_personality["Паспортные данные"].items():
        print(f"{key}: {value}")
    print("\nКредитная история:")
    for key, value in generated_personality["Кредитная история"].items():
        print(f"{key}: {value}")
    print("\nИнтересы и хобби:")
    if "Интересы и хобби" in generated_personality:
        for key, value in generated_personality["Интересы и хобби"].items():
            print(f"{key}: {value}")
