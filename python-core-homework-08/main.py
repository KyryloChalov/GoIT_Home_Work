from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):

    if users == []:
        users = {}

        
    result = {}
    
    WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    list_for_weekday = [[], [], [], [], [], [], []]
    
    d_today = date.today() 
    # d_today = date(year=2023, month=10, day=2) # для отладки
    d_end = d_today + timedelta(days=7)
    
    for user in users:
        # якщо дн вже минув - перенести його на наступний рік
        user["birthday"] = datetime(year=d_today.year, month=user["birthday"].month, day=user["birthday"].day)
        if user["birthday"].date() < d_today:
            user["birthday"] = user["birthday"].replace(year=d_today.year+1)
        
        # вираховуємо день тижня для дн юзера, якщо до нього не більше тижня
        if user["birthday"].date() < (d_end):
            
            # якщо сьогодні - не понеділок, переносимо вихідні на понеділок (наступного тижня)
            # якщо сьогодні понеділок, дн що припали на вихідні виводятся у вихідні 
            # (може прибрати их зовсім??? бо на сьогодняшній понеділок переносити не можна)
            if d_today.weekday() != 0 and user["birthday"].weekday() in [5, 6]: 
                list_for_weekday[0].append(user["name"])
            else:
                # запісати ім'я у відповідний список, з яких потім зробити словник
                list_for_weekday[user["birthday"].weekday()].append(user["name"])
                                
    # збираємо словник з днів тижня та списків юзерів, що мають дн у конкретний день тижня
    for i in range(len(WEEKDAYS)):
        if list_for_weekday[i] != []:     # порожні дні тижня пропускаємо
            result.update({WEEKDAYS[i] : list_for_weekday[i]})
    
    return result 


if __name__ == "__main__":
    users = [
        {"name": "1. Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "2. Bill Gates", "birthday": datetime(1955, 12, 28).date()},
        {"name": "3. John", "birthday": datetime(2000, 10, 2).date()},
        {"name": "4. Doe", "birthday": datetime(1955, 1, 28).date()},
        {"name": "5. Johnfh", "birthday": datetime(1956, 3, 28).date(),},
        {"name": "6. Doedffhg", "birthday": datetime(1963, 10, 8).date(),},
        {"name": "7. Alice", "birthday": datetime(1958, 10, 4).date()},
        {"name": "8. Johnkjnhg", "birthday": datetime(1985, 9, 22).date(),},
        {"name": "9. Doesdf", "birthday": datetime(2001, 1, 8).date(),},
        {"name": "10. Aliceoi", "birthday": datetime(1983, 10, 7).date()}
    ]

    result = get_birthdays_per_week(users)

    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
