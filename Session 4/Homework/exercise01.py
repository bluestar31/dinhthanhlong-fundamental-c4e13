inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocket'] = ['seashell', 'strangeberry', 'lint']
print('Inventory: \n',inventory,'\n')

backpack_list = inventory['backpack']
backpack_list.remove('dagger')
print("Value of 'backpack' key now: ",backpack_list,'\n')

inventory['gold'] += 50
print("Value of 'gold' key now: ",inventory['gold'])
