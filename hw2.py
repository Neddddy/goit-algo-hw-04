# Завдання 2
# Варіант компактніший, зробив з чатом ЖПТ, для неї потрібен імпорт csv
# import csv
# def get_cats_info(path):
#     try:
#         with open(path, "r", encoding="utf-8") as file:
#             reader = csv.DictReader(file, fieldnames=["ID", "Name", "Age"])
#             return list(reader)
#     except FileNotFoundError and OSError:
#         return "Файл пошкоджений або не знайдений!!!"
# Варіант який зробив сам, і той і той працює
def get_cats_info(path):
    liist = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for i in file:
                b = i.strip().split(",")
                cats = {
                    "id" : b[0],
                    "name" : b[1],
                    "age" : b[2]
                }
                liist.append(cats)
            return liist
    except FileNotFoundError and OSError:
        return "Файл пошкоджений або не знайдений!!!"
    
print(get_cats_info(input("Введіть шлях до файлу з інформацією: ")))
