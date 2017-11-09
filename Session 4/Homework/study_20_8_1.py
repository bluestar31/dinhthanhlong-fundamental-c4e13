# Solution 1
string = 'ThiS is String with Upper and lower case Letters'

string = string.lower()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

letter_count = {}
for char in string:
    if char in alphabet: # ignore any punctuation, numbers, etc
        if char in letter_count:
            letter_count[char] = letter_count[char] + 1
        else:
            letter_count[char] = 1

keys = letter_count.keys()
for char in sorted(keys):
    print(char, letter_count[char])

# Solution 2
# string = input("Enter a sentence")
# string = 'ThiS is String with Upper and lower case Letters'
#
# list_string = list(string.lower())
# list_string.sort()
# string = str(list_string)
#
# for ch in [",", "[", "]", "'"]:
#     if ch in string:
#         string = string.replace(ch, "")
#
# letter_counts = {}
#
# for letter in string.replace(" ", ""):
#     letter_counts[letter] = letter_counts.get(letter, 0) + 1
#
# for key, value in letter_counts.items():
#     print(key, value)
