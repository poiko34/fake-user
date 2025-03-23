#!/usr/bin/env python3

import random
import faker
import argparse
from faker.providers import credit_card

# Создаем объект faker
fake = faker.Faker()
fake.add_provider(credit_card)

# Списки для новых данных
passport_issuers = {"ru": ["Отдел МВД России", "Государственный центр", "ФМС", "УФМС"],
                    "pl": ["Wydział Policji", "Centrum Administracyjne", "Urząd Miasta"],
                    "us": ["Department of Motor Vehicles", "Social Security Administration"]}

credit_history = {
    "ru": ["Чистая", "Есть задолженность", "Ипотека", "Кредит на автомобиль", "Нет кредитов"],
    "pl": ["Czysta", "Zadłużenie", "Kredyt hipoteczny", "Kredyt samochodowy", "Brak kredytów"],
    "us": ["Clear", "Debt", "Mortgage", "Car Loan", "No Credit"]
}

# Функция для определения пола по имени (условная логика)
def determine_gender(name):
    if name.endswith('а') or name.endswith('я'):
        return "Женщина"
    else:
        return "Мужчина"

# Функция генерации случайной личности
def generate_extended_fake_personality(level=1, country="ru"):
    # Настройка фейкера в зависимости от страны
    if country == "pl":
        fake = faker.Faker('pl_PL')
    elif country == "us":
        fake = faker.Faker('en_US')
    else:
        fake = faker.Faker('ru_RU')

    # Общие данные
    name = fake.name()
    gender = determine_gender(name)
    age = random.randint(18, 60)
    phone_number = fake.phone_number()

    if level == 1:
        return {
            "Имя": name,
            "Возраст": age,
            "Пол": gender,
            "Телефон": phone_number
        }

    if level >= 2:
        passport_series = f"{random.randint(10, 99)}"
        passport_number = f"{random.randint(100000, 999999)}"
        passport_issue_date = fake.date_this_century()
        passport_issuer = random.choice(passport_issuers.get(country, passport_issuers["ru"]))
        passport_code = f"{random.randint(1000, 9999)}"
        passport_firstname = name.split()[1]
        passport_lastname = name.split()[0]
        passport_patronymic = fake.first_name_male() if country == "ru" else ""
        passport_birthdate = fake.date_of_birth(minimum_age=18, maximum_age=60)
        passport_gender = gender
        passport_nationality = "Россия" if country == "ru" else ("Polska" if country == "pl" else "USA")
        passport_address = fake.address()
        passport_signature = "Подпись владельца паспорта" if country == "ru" else "Signature of passport holder"
        passport_photo = "Фото владельца паспорта" if country == "ru" else "Passport holder's photo"

        credit_score = random.choice(["Высокий", "Средний", "Низкий"] if country == "ru" else ["High", "Medium", "Low"])
        credit_status = random.choice(credit_history.get(country, credit_history["ru"]))

        return {
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

# Создаем парсер аргументов
parser = argparse.ArgumentParser(description="Генерация фейковых данных")
parser.add_argument('-c', '--country', type=str, choices=['ru', 'pl', 'us'], default='ru', help="Выберите страну: ru - Россия, pl - Польша, us - США")
parser.add_argument('-l', '--level', type=int, choices=[1, 2], default=1, help="Выберите уровень генерации (1 - базовые данные, 2 - паспортные и кредитные данные)")

# Парсим аргументы
args = parser.parse_args()

# Генерация данных
generated_personality = generate_extended_fake_personality(args.level, args.country)

# Вывод результата
print("\nГенерированные данные:")
if args.level == 1:
    for key, value in generated_personality.items():
        print(f"{key}: {value}")
elif args.level == 2:
    print("\nОсновная информация:")
    for key, value in generated_personality["Основная информация"].items():
        print(f"{key}: {value}")
    print("\nПаспортные данные:")
    for key, value in generated_personality["Паспортные данные"].items():
        print(f"{key}: {value}")
    print("\nКредитная история:")
    for key, value in generated_personality["Кредитная история"].items():
        print(f"{key}: {value}")
