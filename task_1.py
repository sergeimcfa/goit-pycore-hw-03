# task_1.py
# -----------------------------
# Домашнє завдання: Робота з датою, часом та рядками
# Завдання 1: Обчислити кількість днів між заданою датою і поточною датою
# -----------------------------

from datetime import datetime


def get_days_from_today(date):

    try:
        # Перетворюємо рядок дати у об’єкт datetime.date
        target_date = datetime.strptime(date, "%Y-%m-%d").date()

        # Отримуємо поточну дату
        today = datetime.today().date()

        # Розраховуємо різницю у днях
        delta = today - target_date

        # Повертаємо різницю у днях
        return delta.days

    except ValueError:
        # Якщо формат дати невірний
        return "Помилка: неправильний формат дати. Використовуйте 'YYYY-MM-DD'."


# -----------------------------
# Приклади виконання
# -----------------------------
if __name__ == "__main__":
    print(get_days_from_today("2021-10-09"))   # Приклад: -157 (якщо сьогодні 2021-05-05)
    print(get_days_from_today("2020-10-09"))   # Приклад: 208
    print(get_days_from_today("202a-01-01"))   # Приклад: повідомлення про помилку
