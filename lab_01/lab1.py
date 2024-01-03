# Initial sorted list
list = [
    {"name": "Bob", "phone": "0631234567", 'email': 'Bob@gmail.com', 'group': 'KB221'},
    {"name": "Emma", "phone": "0631234567", 'email': 'Emma@gmail.com', 'group': 'KB222'},
    {"name": "Jon", "phone": "0631234567", 'email': 'jonweek@gmail.com', 'group': 'AM211'},
    {"name": "Zak", "phone": "0631234567", 'email': 'izak@gmail.com', 'group': 'KI105'}
]

def printAllList():
    for elem in list:
        strForPrint = f"Student name is {elem['name']}, Phone is {elem['phone']}, E-mail is {elem['email']}, Group is {elem['group']}"
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student name: ").capitalize()
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")
    newItem = {"name": name, "phone": phone, 'email': email, 'group': group}
    
    # Insert at the correct position
    list.append(newItem)
    list.sort(key=lambda x: x['name'])
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    for idx, item in enumerate(list):
        if name == item["name"]:
            del list[idx]
            print("Element has been deleted")
            return
    print("Element was not found")
    return

def updateElement():
    name = input("Please enter name to be updated: ")
    for idx, elem in enumerate(list):
        if elem['name'] == name:
            new_name = input("Please enter new student name: ").capitalize()
            list[idx]['name'] = new_name
            list.sort(key=lambda x: x['name'])
            print("Element has been updated")
            return
    print("Element not found")
    return

def main():
    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit]: ").upper()
        if choice == "C":
            print("New element will be created:")
            addNewElement()
            printAllList()
        elif choice == "U":
            print("Existing element will be updated")
            updateElement()
            printAllList()
        elif choice == "D":
            print("Element will be deleted")
            deleteElement()
            printAllList()
        elif choice == "P":
            print("List will be printed")
            printAllList()
        elif choice == "X":
            print("Exiting...")
            break
        else:
            print("Wrong choice")

main()