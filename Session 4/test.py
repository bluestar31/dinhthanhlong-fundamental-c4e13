# p = ['Tuan anh', 22, 3, 'Moc Chau', 2]
# print(p)

# person = {}
# print(person)

# person = {
#     'name': 'Tuan Anh'
# }
#
# print(person)

# person = {
#     'name': 'Tuan Anh',
#     'age': 22,
#     'home': 'Moc Chau',
# }
#
# print(person['home'])
# person['home'] = 'Ha Noi'
# print(person)
#
# person['project_count'] = 2
# print(person)

string = "Heello I'm Long"

letter_counts = {}

for letter in string.replace(" ", ""):
    letter_counts[letter.lower()] = letter_counts.get(letter, 0) + 1
print(letter_counts)
# for letter in string.replace(" ", ""):
#     print(letter_counts.get(letter, 0) + 1 )
