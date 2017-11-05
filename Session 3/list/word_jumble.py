from random import choice

word = 'handsome'

characters = list(word)

word_after_jumb = choice(characters)
characters.remove(word_after_jumb)

print(word_after_jumb, sep = ' ')
