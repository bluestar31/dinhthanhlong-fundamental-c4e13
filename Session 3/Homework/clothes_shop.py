clothes_list = ['T-Shirt', 'Sweater', 'Jeans']
logic = True

question = input("Welcome to our shop, what do you want (C, R, U, D)? ")
if question.upper() == 'C':
    new_item = input("Enter new item: ")
    clothes_list.append(new_item)
    print(*clothes_list, sep = ", ")
elif question.upper() == 'R':
    print(*clothes_list, sep = ", ")
elif question.upper() == 'U':
    while logic:
        update_position = int(input("Update position: "))
        if update_position < -1:
            print("The number is not accepted! Please input another number!")
        else:
            logic = False
    new_item_update = input("New item? ")
    clothes_list[update_position] = new_item_update
    print(*clothes_list, sep = ", ")
elif question.upper() == 'D':
    while logic:
        delete_position = int(input("Delete position: "))
        if delete_position < -1:
            print("The number is not accepted! Please input another number!")
        else:
            logic = False
    clothes_list.remove(clothes_list[delete_position])
    print(*clothes_list, sep = ", ")
