from datetime import datetime, date, timedelta

def get_upcoming_birthdays(users):
    
    today = datetime.today().date()
    upcoming_birthdays_list = []

    for user in users:
        try:
            # 1. Конвертуємо рядок дати народження в об'єкт date
            birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        except ValueError:
            # Обробка можливої помилки формату дати
            print(f"Некоректний формат дати для {user['name']}: {user['birthday']}")
            continue

        # 2. Визначаємо дату наступного дня народження
        
        # Обробка високосного року (29 лютого)
        try:
            birthday_this_year = birthday_date.replace(year=today.year)
        except ValueError:
            # Виникає, якщо ДН 29.02, а поточний рік - не високосний
            # У такому разі, "день народження" святкується 1 березня
            birthday_this_year = date(today.year, 3, 1)

        # 3. Перевіряємо, чи день народження вже минув у цьому році
        if birthday_this_year < today:
            # Якщо так, розглядаємо дату наступного року
            try:
                birthday_next_occurrence = birthday_this_year.replace(year=today.year + 1)
            except ValueError:
                 # Обробка 29.02, якщо наступний рік - не високосний
                birthday_next_occurrence = date(today.year + 1, 3, 1)
        else:
            # Якщо ні, то беремо дату цього року
            birthday_next_occurrence = birthday_this_year
            
        # 4. Визначаємо різницю між днем народження та поточною датою
        delta_days = (birthday_next_occurrence - today).days

        # 5. Перевіряємо, чи день народження потрапляє у 7-денний інтервал
        # (від 0 [сьогодні] до 6 [включно 7-й день])
        if 0 <= delta_days < 7:
            
            # 6. Визначаємо день тижня (0=Пн, 1=Вт, ..., 5=Сб, 6=Нд)
            weekday = birthday_next_occurrence.weekday()
            
            congratulation_date = birthday_next_occurrence

            # 7. Переносимо дату привітання, якщо ДН припадає на вихідний
            if weekday == 5:  # Субота
                congratulation_date += timedelta(days=2)  # Переносимо на Понеділок
            elif weekday == 6:  # Неділя
                congratulation_date += timedelta(days=1)  # Переносимо на Понеділок

            # 8. Форматуємо дату привітання назад у рядок
            congratulation_date_str = congratulation_date.strftime("%Y.%m.%d")
            
            # 9. Додаємо користувача до списку привітань
            upcoming_birthdays_list.append({
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })

    return upcoming_birthdays_list

# --- Приклад використання ---

users = [
    {"name": "John Doe", "birthday": "1985.01.23"}, # Вівторок (23.01) -> 23.01
    {"name": "Jane Smith", "birthday": "1990.01.27"}, # Субота (27.01) -> 29.01 (Пн)
    {"name": "Peter Pen", "birthday": "1992.01.22"}, # Сьогодні (22.01) -> 22.01
    {"name": "Sam Wise", "birthday": "1993.01.28"}, # Неділя (28.01) -> 29.01 (Пн)
    {"name": "Sara Connor", "birthday": "1988.01.29"}, # Понеділок (29.01) -> Не входить (понад 7 днів)
    {"name": "Mike Tyson", "birthday": "1970.01.19"}  # Минулий (19.01) -> Не входить
]

# Для запуску та перевірки:
# (Результат буде залежати від поточної дати запуску коду)
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
