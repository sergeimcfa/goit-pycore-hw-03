# task_2.py
# -----------------------------
# Домашнє завдання: Робота з датою, часом та рядками
# Завдання 2: Генерація унікальних випадкових чисел для лотереї
# -----------------------------

import random


def get_numbers_ticket(min, max, quantity):

    # Перевіряємо коректність вхідних даних
    if not (1 <= min < max <= 1000):
        return []
    if not (0 < quantity <= (max - min + 1)):
        return []

    # Генеруємо унікальні випадкові числа
    numbers = random.sample(range(min, max + 1), quantity)

    # Повертаємо відсортований список
    return sorted(numbers)
