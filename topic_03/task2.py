# Створення тестового списку
my_list = [1, 2, 3]

# Тестування функцій списків
my_list.extend([4, 5])
print(f"extend(): {my_list}")

my_list.append(6)
print(f"append(): {my_list}")

my_list.insert(1, 10)
print(f"insert(1, 10): {my_list}")

my_list.remove(3)
print(f"remove(3): {my_list}")

my_list.clear()
print(f"clear(): {my_list}")

my_list = [4, 2, 1, 3]
my_list.sort()
print(f"sort(): {my_list}")

my_list.reverse()
print(f"reverse(): {my_list}")

my_list_copy = my_list.copy()
print(f"copy(): {my_list_copy}")