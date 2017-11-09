import string

infile = open('alice_in_wonderland.txt', 'r')

text = infile.readlines()

counts = {}

for line in text:
	for word in line:
		counts[word] = counts.get (word, 0) +1
'''
if word != " ":
	if word != ".":
'''			


word_keys = counts.keys()
word_keys.sort()


	
	

infile.close()

outfile = open("alice_words.txt", 'w')
outfile.write("Word \t \t Count \n")
outfile.write("======================= \n")
for word in word_keys:
	outfile.write("%-12s%d\n" % (word.lower(), counts[word]))
outfile.close()
