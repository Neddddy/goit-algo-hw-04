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
                summ += float(i[1])
            average = summ/len(linez)
        return summ, average
    except (FileNotFoundError, OSError, ZeroDivisionError) :
        return None

result = total_salary(input("Введіть шлях до файлу: "))
if result:
    total, average = result
    print(f"Загальна сума заробітної плати: {total}, cередня заробітна плата: {average}")
else:
    print("Файл пустий або пошкоджений!!!")
