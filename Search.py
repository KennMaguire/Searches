#need to fix python 3 profile
"""
Kenneth Maguire
Python 3 Program

Search.py
This program add the works of shakespeare to a dictionary and determines how many of each word exists
The program does this through unsorted, sorted, and hash searching methods.



"""



import string
import time

def unsortedSearch(_unsortedDict, _searchKey):

    for k,v in _unsortedDict.items():
        if k == _searchKey:
            #print(1)
            _unsortedDict[_searchKey] = v + 1
        #    print(k,v)
            return _unsortedDict

    #print(2)
    _unsortedDict[_searchKey] = 1
    return _unsortedDict







filename = "shakespeare.txt"
f = open(filename, 'r')

t0 = time.process_time()
wordList = []

dict_of_words_unsorted = {}

for line in f:
    line = line.translate(str.maketrans('','',string.punctuation)) #remove punctuation from input sequence  https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
    for word in line.split():
        wordLow = word.lower()      #set word to lower case
        #wordList.append(wordLow)
        dict_of_words_unsorted = unsortedSearch(dict_of_words_unsorted, wordLow)
        f"\n {t0}"
        print(dict_of_words_unsorted)




print("Process time = ")
print(t0)
print("\n")


print(dict_of_words_unsorted)

i = 0
while i < 100:
    print(wordList[i])
    i += 1
i = (len(wordList) - 100)
while i < len(wordList):
    print(wordList[i])
    i += 1
