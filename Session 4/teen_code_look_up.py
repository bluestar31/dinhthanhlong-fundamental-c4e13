teen_dict = {
    'thui': 'thôi',
    'iu': 'yêu',
    'ck': 'chồng',
    'cl': 'củ lạc',
    'clgt': 'củ lạc giòn tan'
}

print(*teen_dict, sep = "       ")

input_code = input('Which word do you want to look up? ')
print("Code: ", input_code)
while True:
    if input_code in teen_dict:
        print('Translation: ',teen_dict[input_code])
        quit = input('Do you want to try another word? (Y/N) ')
        if quit.upper() == 'Y':
            input_code = input('Which word do you want to look up? ')
            print("Code: ", input_code)
        elif quit.upper() == 'N':
            break
    else:
        ask = input("Not found, do you want to create a new word? (Y/N) ")
        if ask.upper() == 'Y':
            new_word = input('Enter your translation: ')
            teen_dict[input_code] = new_word
            print('Updated')
            quit = input('Do you want to try another word? (Y/N) ')
            if quit.upper() == 'Y':
                input_code = input('Which word do you want to look up? ')
                print("Code: ", input_code)
            elif quit.upper() == 'N':
                break
            print(*teen_dict, sep = "       ")
        elif ask.upper() == 'N':
            quit = input('Do you want to try another word? (Y/N) ')
            if quit.upper() == 'Y':
                input_code = input('Which word do you want to look up? ')
                print("Code: ", input_code)
            elif quit.upper() == 'N':
                break
