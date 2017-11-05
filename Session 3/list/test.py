# # menu = ['com', 'bun', 'pho']
# # print(*menu, sep = ', ')
# #
# # print('* ' * 20)
# #
# # menu.remove('bun')
# # print(*menu, sep = ', ')
# #
# # if 'chan ga' in menu:
# #     menu.remove('chan ga')
# # else:
# #     print('chan ga khong co trong list')
#
# menu = ['com', 'bun', 'pho', 'nem', 'com rang']
#
# # print(len(menu))
#
# # for item in menu:
# #     print(item.upper())
#
# # for i in range(len(menu)):
# #     print(i, menu[i])
#
# # print(menu[-1])
#
# # for index, item in enumerate(menu):
# #     print(index + 1, '. ', item, sep = '')
#
# menu[1] = 'cha xien'
# print(*menu, sep = ', ')
#
# print(menu[4])

from random import choice

s = 'Hello'
characters = list(s)
c = choice(characters)
