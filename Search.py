import re

import string

filename = "shakespeare.txt"
f = open(filename, 'r')


wordList = []

for line in f:
    line = line.translate(None, string.punctuation) #remove punctuation from input sequence
    for word in line.split():
        wordList.append(word)

i = 0
while i < 100:
    print(wordList[i])
    i += 1
i = (len(wordList) - 100)
while i < len(wordList):
    print(wordList[i])
    i += 1
