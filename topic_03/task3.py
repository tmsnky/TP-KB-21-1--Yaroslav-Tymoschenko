# Створення тестового словника
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Тестування функцій словників
my_dict.update({'d': 4, 'e': 5})
print(f"update(): {my_dict}")

del my_dict['a']
print(f"del('a'): {my_dict}")

my_dict.clear()
print(f"clear(): {my_dict}")

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(f"keys(): {my_dict.keys()}")
print(f"values(): {my_dict.values()}")
print(f"items(): {my_dict.items()}")