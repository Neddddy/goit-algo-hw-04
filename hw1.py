# Завдання 1
def total_salary(path):
    summ = 0
    linez = []
    try:
        with open(path , "r", encoding="utf-8") as zarplata:
            lines = [line.strip() for line in zarplata.readlines()]
            for i in lines:
                linez.append(i.split(","))
            for i in linez:
                summ += int(i[1])
    except FileNotFoundError and OSError:
        return "Файл пошкоджений або не знайдений!!!"
    return f"Загальна сума заробітної плати: {summ}, Середня заробітна плата: {int(summ/len(linez))}"
print(total_salary(input("Введіть шлях до файлу: ")))