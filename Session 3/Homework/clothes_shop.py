clothes_list = ['T-Shirt', 'Sweater', 'Jeans']
logic = True
menu = True

while menu:
    question = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    if question.upper() == 'C':
        new_item = input("Enter new item: ")
        clothes_list.append(new_item)
        print(*clothes_list, sep = ", ")
    elif question.upper() == 'R':
        print(*clothes_list, sep = ", ")
    elif question.upper() == 'U':
        while True:
            update_position = int(input("Update position: "))
            if update_position < 1 or update_position > len(clothes_list):
                print("The number is not accepted! Please input another number!")
            else:
                break
        new_item_update = input("New item? ")
        clothes_list[update_position - 1] = new_item_update
        print(*clothes_list, sep = ", ")
    elif question.upper() == 'D':
        while True:
            delete_position = int(input("Delete position: "))
            if delete_position < 1 or delete_position > len(clothes_list):
                print("The number is not accepted! Please input another number!")
            else:
                break
        clothes_list.remove(clothes_list[delete_position - 1])
        print(*clothes_list, sep = ", ")
    ask = input("Do you want to countinue with our shop? (Y/N) ")
    if ask.upper() == "Y":
        menu = True
    elif ask.upper() == "N":
        menu = False
