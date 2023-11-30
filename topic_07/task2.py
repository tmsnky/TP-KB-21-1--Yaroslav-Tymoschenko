class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Створення списку об'єктів класу Student
students = [
    Student("Alice", 20),
    Student("Bob", 22),
    Student("Charlie", 19),
    Student("Yaroslav", 18),
    Student("Diana", 17)
]

# Сортування списку студентів за віком за допомогою функції sorted і lambda
sorted_students = sorted(students, key=lambda x: x.age)

# Виведення на екран відсортованого списку студентів
for student in sorted_students:
    print(f"Name: {student.name}, Age: {student.age}")