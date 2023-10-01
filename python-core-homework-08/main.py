"""
    Домашне завдання № 8: реалізувати функцію для виведення списку колег, яких потрібно привітати з днем народження на тижні.
        ### version 1.3.2
    особливості реалізації:
    21-22   - якщо список користувачів порожній
    27      - визначаємо сьогодняшню дату через date.today() 
    28      - рядок для тестування
    30-31   - якщо сьогодні понеділок - треба вивести дн за минулі вихідні, а наступні вихідні - вимкнути
    33-34   - якщо сьогодні неділя - треба врахувати вчорашні дн (за суботу)
    40      - переносимо дату дн на поточний рік
    42-43   - якщо дн вже минув - перенести його на наступний рік (на 365 days)
    45-49   - вираховуємо день тижня для дн юзера, якщо до нього не більше тижня. формуємо списки юзерів з дн по днях тижня
    46-47   - якщо дн випадає на вихідні - переносимо їх на наступний понеділок
    51-54   - збираємо словник з днів тижня та списків юзерів, що мають дн у конкретний день тижня
    53      - порожні дні тижня пропускаємо
"""
from datetime import date, datetime, timedelta
    
def get_birthdays_per_week(users):

    if users == []:
        users = {}

    WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    list_for_weekdays = [[], [], [], [], [], [], []]
    
    d_today = date.today() 
    # d_today = date(year=2023, month=10, day=3) # рядок для тестування!
    
    if d_today.weekday() == 0: 
        d_today = d_today + timedelta(-2)
    
    if d_today.weekday() == 6: 
        d_today = d_today + timedelta(-1)
    
    d_end = d_today + timedelta(7)
        
    for user in users:
        
        user["birthday"] = datetime(year=d_today.year, month=user["birthday"].month, day=user["birthday"].day)
        
        if user["birthday"].date() < d_today:
            user["birthday"] = user["birthday"] + timedelta(365)
         
        if user["birthday"].date() < (d_end):
            if user["birthday"].weekday() in [5, 6]: 
                list_for_weekdays[0].append(user["name"])
            else:
                list_for_weekdays[user["birthday"].weekday()].append(user["name"])
                
    users = {}
    for i in range(len(WEEKDAYS)):
        if list_for_weekdays[i] != []: 
            users.update({WEEKDAYS[i] : list_for_weekdays[i]})
    
    return users 


if __name__ == "__main__":
    users = [               # дані для тестування
        {"name": "1. Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "2. Bill Gates", "birthday": datetime(1955, 12, 28).date()},
        {"name": "3. John", "birthday": datetime(2000, 10, 2).date()},
        {"name": "4. Doe", "birthday": datetime(1955, 1, 28).date()},
        {"name": "5. Johnfh", "birthday": datetime(1956, 3, 28).date(),},
        {"name": "6. Doedffhg", "birthday": datetime(1963, 10, 8).date(),},
        {"name": "7. Alice", "birthday": datetime(1958, 10, 4).date()},
        {"name": "8. Johnkjnhg", "birthday": datetime(1985, 10, 1).date(),},
        {"name": "9. Doesdf", "birthday": datetime(2001, 10, 6).date(),},
        {"name": "10. Aliceoi", "birthday": datetime(1983, 10, 7).date()}
    ]

    result = get_birthdays_per_week(users)

    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
