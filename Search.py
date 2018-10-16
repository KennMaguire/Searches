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

from itertools import islice
import re
#this function was found on stackoverflow for slicing a dictionary
#https://stackoverflow.com/questions/7971618/python-return-first-n-keyvalue-pairs-from-dict
def takeFirst(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))
#gets a slice of the last 10 items in the dictionary
def takeLast(n, iterable):
    return list(islice(iterable, n, None))

class comparisonCounter:
    total = 0
    def __init__(self):
        self.total = 0
    def add(self, x):
        self.total += x

class assignmentCounter:
    total = 0
    def __init__(self):
        self.total = 0
    def add(self, x):
        self.total += x


def unsortedSearch(_unsortedDict, _searchKey, _assign, _comp):
    for k,v in _unsortedDict.items():
        _comp.add(1)
        if k == _searchKey:
            #print(1)
            _unsortedDict[_searchKey] = v + 1
        #    print(k,v)
            return _unsortedDict

    #print(2)
    _assign.add(1)
    _unsortedDict[_searchKey] = 1
    return _unsortedDict







filename = "wordlist.txt"
f = open(filename, 'r')

start_time = time.time()
wordList = []
d_w_unsorted = {}
assignInt = assignmentCounter()
compInt = comparisonCounter()

for line in f:
    line = line.translate(str.maketrans('','', '!.@"$?&:;,/()*^%>+=|<}{[]'))   #remove punctuation from input sequence  https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
    line = re.sub('[0-9]', '', line)                               #remove numbers https://stackoverflow.com/questions/35256946/python-3x-remove-numbers-from-file-names
    for word in line.split():
        wordLow = word.lower()      #set word to lower case
        wordLow = wordLow.replace(wordLow, "") if wordLow.startswith("'") else wordLow
        #wordList.append(wordLow)
        d_w_unsorted = unsortedSearch(d_w_unsorted, wordLow, assignInt, compInt)
                                                                                                #https://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/ for help with sorting and printing
        #d_w_unsorted = sorted(d_w_unsorted)
        #print(sorted(d_w_unsorted))

#print(d_w_unsorted)

d_w_unsorted.pop("'", None)
d_w_unsorted.pop('"', None)
d_w_unsorted.pop('', None)

print("The first 10 words are: ")
n_items = takeFirst(10, d_w_unsorted.items())
for k,v in n_items:
    print(k,v)
print("\n\n")
listLenMin10 = len(d_w_unsorted) - 10
print("The first 10 words are: ")
n_items = takeLast(listLenMin10, d_w_unsorted.items())
for k,v in n_items:
    print(k,v)
print("\n\n")

print("The number of comparisons is: " + str(compInt.total))
print("The number of assignments is: " + str(assignInt.total))


print("Process time = ")
print(time.time() - start_time)
print("\n")

print("The number of unique words is: ")
print(len(d_w_unsorted))
print("\n")


d_w_unsorted = sorted(d_w_unsorted.items())


#print(d_w_unsorted)

#now do it for the sorted dictionary

print("The number of unique words is: ")
print(len(d_w_unsorted))
print("\n")


"""
print("The first 10 words are: ")
#n_items = takeFirst(10, d_w_unsorted.items())
"""

"""
print("The first 10 words are: ")
for k,v in d_w_unsorted[0:10]:
    print(k,v)
print("\n\n")
listLenMin10 = len(d_w_unsorted) - 10
print("The last 10 words are: ")
#n_items = takeLast(listLenMin10, d_w_unsorted.items())
for k,v in d_w_unsorted[listLenMin10:len(d_w_unsorted)]:
    print(k,v)
print("\n\n")

"""
f2 = open("wordListSorted.txt", "w")


for k,v in d_w_unsorted:
    f2.write("%s\n" % k)

print("The number of comparisons is: " + str(compInt.total))
print("The number of assignments is: " + str(assignInt.total))


print("Process time = ")
print(time.time() - start_time)
print("\n")







"""

i = 0
while i < 100:
    print(wordList[i])
    i += 1
i = (len(wordList) - 100)
while i < len(wordList):
    print(wordList[i])
    i += 1
"""
