from random import choice

print("Welcome to the hangman game!")
image = [
"""
______
|    |
|    o
|
|
|_
""",
"""
______
|    |
|    o
|    |
|
|_
""",
"""
______
|    |
|    o
|  --|
|
|_
""",
"""
______
|    |
|    o
|  --|--
|
|_
""",
"""
______
|    |
|    o
|  --|--
|   /
|_
""",
"""
______
|    |
|    o
|  --|--
|   / \\
|_
"""
]


word_list = ['apple', 'orange', 'peach', 'strawberry', 'rasberry']
word_random = choice(word_list)

word_space = '_' * len(word_random)
word_space_list = list(word_space)

characters = list(word_random)

count = 1

print(image[0])

while count <= 5:
    print(*word_space_list, sep = ' ')
    guess = input('Guess any characters? ')
    if guess in characters:
        for index, character in enumerate(characters):
            if character == guess:
                guess_index = index
                word_space_list[guess_index] = guess
    else:
        print(image[count])
        count += 1
        if count > 5:
            print(image[count - 1])
            print(*word_space_list, sep = ' ')
            print('You lose!')
    if '_' not in word_space_list:
        print(*word_space_list, sep = ' ')
        print('You win!')
        break
