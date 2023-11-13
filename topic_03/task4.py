def find_insert_position(sorted_list, new_element):
    for i, element in enumerate(sorted_list):
        if new_element <= element:
            return i
    return len(sorted_list)

sorted_list = [1, 3, 5, 7, 9]
new_element = 6
insert_position = find_insert_position(sorted_list, new_element)
print(f"The new element {new_element} should be inserted at position {insert_position}")