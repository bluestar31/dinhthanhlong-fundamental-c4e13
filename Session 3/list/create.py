menu = [1, 2, 3, 4]

new_item = input('What do u want to add? ')
# menu.append(create)
menu.insert(0, new_item)

print(*menu, sep = ', ')
