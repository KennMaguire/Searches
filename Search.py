filename = "shakespeare.txt"
f = open(filename, 'r')


wordList = []

for line in f:
    for word in line.split():
        wordList.append(word)

i = 0
while i < 10:
    print(wordList[i])
    i += 1
i = (len(wordList) - 10)
while i < len(wordList):
    print(wordList[i])
    i += 1
