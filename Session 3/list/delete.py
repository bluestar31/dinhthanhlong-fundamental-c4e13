menu = ['bun', 'cha', 'ga quay']
print(*menu, sep = ', ')

item_to_remove = input("Nhap vao mon muon xoa? ")
if item_to_remove in menu:
    menu.remove(item_to_remove)
else:
    print(item_to_remove, 'khong ton tai')
print(*menu, sep = ', ')
