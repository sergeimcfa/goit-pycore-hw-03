# task_4.py
# -----------------------------
# Домашнє завдання: Робота з датою, часом та рядками
# Завдання 4: Список привітань з днями народження на 7 днів уперед
# -----------------------------

from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    """
    Повертає список словників з іменем користувача та датою привітання
    для всіх днів народження, що припадають на наступні 7 днів (включно з сьогоднішнім).
    Якщо день народження у вихідні (субота/неділя), дата привітання переноситься на наступний понеділок.

    Аргументи:
        users (list[dict]): Список словників з ключами:
            - name (str): Ім'я користувача
            - birthday (str): Дата народження у форматі 'YYYY.MM.DD'

    Повертає:
        list[dict]: Список словників виду:
            {'name': <name>, 'congratulation_date': 'YYYY.MM.DD'}
    """
    today = datetime.today().date()
    result = []

    for user in users:
        try:
            bday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        except (KeyError, ValueError):
            # Пропускаємо некоректні записи
            continue

        # День народження у поточному році
        bday_this_year = bday.replace(year=today.year)

        # Якщо вже минув цього року — беремо наступний рік
        if bday_this_year < today:
            bday_this_year = bday_this_year.replace(year=today.year + 1)

        # Різниця у днях до дня народження
        delta_days = (bday_this_year - today).days

        # Беремо лише ті, що в межах наступних 7 днів (включно з сьогодні)
        if 0 <= delta_days <= 7:
            congrats_date = bday_this_year

            # Якщо це субота (5) або неділя (6) — переносимо на понеділок
            if congrats_date.weekday() >= 5:
                # Скільки днів додати, щоб отримати понеділок (weekday() == 0)
                days_to_monday = 7 - congrats_date.weekday()
                congrats_date = congrats_date + timedelta(days=days_to_monday)

            result.append({
                'name': user.get('name', 'Unknown'),
                'congratulation_date': congrats_date.strftime('%Y.%m.%d')
            })

    return result


# -----------------------------
# Приклади виконання
# -----------------------------
if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
        {"name": "Max Mustermann", "birthday": "1992.02.29"},  # перевірка високосних дат
    ]

    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)
