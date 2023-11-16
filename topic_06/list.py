# Список студентів
students = [
    {"name": "Іван", "grade": 85},
    {"name": "Марія", "grade": 92},
    {"name": "Олександр", "grade": 88},
    {"name": "Анна", "grade": 94},
    {"name": "Петро", "grade": 91}
]

# Сортування за ім'ям
sorted_by_name = sorted(students, key=lambda x: x['name'])
print("Сортування за ім'ям:")
for student in sorted_by_name:
    print(student)

# Сортування за оцінкою
sorted_by_grade = sorted(students, key=lambda x: x['grade'])
print("\nСортування за оцінкою:")
for student in sorted_by_grade:
    print(student)