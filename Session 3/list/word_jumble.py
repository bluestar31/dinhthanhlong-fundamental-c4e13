from random import choice

word = 'handsome'

characters = list(word)
word_jumble_list = []

while True:
    word_after_jumble = choice(characters)
    characters.remove(word_after_jumble)
    word_jumble_list.append(word_after_jumble)
    if characters == []:
        break

print(*word_jumble_list, sep = ', ')

count = 1
while count <= 5:
    guess = input("Can you guess this word? ")
    if guess.lower() == word:
        print("Bingo! You're so good!")
        break
    else:
        if count < 5:
            print("You're wrong, please try again!", 5 - count, " remaining.")
        else:
            print("You lose!")
    count += 1
