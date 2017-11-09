# Study exercise 20.8.3 & 20.8.4
f = open('alice.txt', 'r')
# text = f.read()
# # f.close()
#
# words = text.split(" ")

count = {}

# for word in words:

# ignore_words = ["{", '[']

for line in f:
    for word in line.split():

            # remove punctuation
        word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
        word = word.replace('?', '').replace('!', '').replace("'", "")
        word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
        word = word.replace(']', '').replace(';', '')

        word = word.lower()

        # ignore numbers
        if word.isalpha():
            if word in count:
                count[word] = count[word] + 1
            else:
                count[word] = 1

f.close()
keys = count.keys()

# save the word count analysis to a file
out = open('alice_words.txt', 'w')
out.write("Word \t \t Count \n")
out.write("======================= \n")

for word in sorted(keys):
    out.write(word + "\t \t" + str(count[word]))
    out.write('\n')

print("The word 'alice' appears",count['alice'],"times in the book.\n")

longest_word = 'alice'

for word in sorted(keys):
    if len(word) >= len(longest_word):
        if word == longest_word:
            break
        else:
            longest_word = word
print("Longest word in Alice in Wonderland is:\n-",longest_word)
for word in sorted(keys):
    if len(word) == len(longest_word):
        print('-',word)
print("Number of characters of longest word is: ",len(longest_word))


out.close()
