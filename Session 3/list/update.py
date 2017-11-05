menu = ['I', 'love', 'you', 'so', 'much']

for index, item in enumerate(menu):
    print(index + 1, '. ', item, sep = '')

position_update = int(input('Position you want to update? '))
replace_item = input('Your replacing favorite? ')

menu[position_update-1] = replace_item
print(*menu, sep = ' ')
