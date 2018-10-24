"""
Kenneth Maguire
Python 3 Program

Run with: python3 SearchSorted.py

SearchSorted.py
This program add the works of shakespeare to a list and determines how many of each word exists
The program does this through an sorted searching method, specifically binary search.


"""











import string
import time
import operator

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

class wordAndValue:
    def __init__(self, wordPassed, value):
        self.word = wordPassed
        self.val = value
    def __lt__(self, other):
        return self.word < other.word
    def __le__(self,other):
        return(self.word <= other.word)






def sortedSearch(_sortedList, _searchKey, _assign, _comp):
    wordV = wordAndValue(_searchKey, 1)

    end = (len(_sortedList)-1)          #end is the length of the list-1
    start = 0


    while start <= end:
        halfway = int((start + end)/2)     #each iteration, start is increased by 1,

        if _searchKey > _sortedList[halfway].word:          #if key is more than halfway value, search top half
            start = halfway + 1
            _comp.add(1)
        elif _searchKey < _sortedList[halfway].word:        #if key is less than halfway value, search bottom half
            _comp.add(1)
            end = halfway - 1

        else:                                               #else, found
            _sortedList[halfway].val += 1                   #if found, add 1 to the value
            _comp.add(1)
            return _sortedList
    #if the key isn't found, add to list at sorted point
    if start >= end:
        _sortedList = _sortedList[:start] + [wordV] + _sortedList[start:]                  #https://stackoverflow.com/questions/14895599/insert-an-element-at-specific-index-in-a-list-and-return-updated-list
        _assign.add(1)
        return _sortedList
    else:
        _sortedList = _sortedList[:halfway] + [wordV] + _sortedList[halfway:]               #https://stackoverflow.com/questions/14895599/insert-an-element-at-specific-index-in-a-list-and-return-updated-list
        _assign.add(1)
        return _sortedList






# start driver code

filename = "wordlist.txt"
f = open(filename, 'r')

start_time = time.time()

assignInt = assignmentCounter()
compInt = comparisonCounter()

sortedList = []

for line in f:
    line = line.translate(str.maketrans('','', '!.@"$?&:;,/()*^%>+=|<}{[]'))   #remove punctuation from input sequence  https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
    line = re.sub('[0-9]', '', line)                                           #remove numbers https://stackoverflow.com/questions/35256946/python-3x-remove-numbers-from-file-names
    for word in line.split():
        wordLow = word.lower()      #set word to lower case
        wordLow = wordLow.strip()
        wordLow = wordLow.replace(wordLow, "") if wordLow.startswith("'") else wordLow
        #wordList.append(wordLow)
        #print(sortedList)

        if not sortedList:
            #print(1)
            firstWordV = wordAndValue(wordLow, 1)
        #    print(sortedList)
            sortedList.append(firstWordV)
        #    print(sortedList)
        if wordLow == "" or wordLow == " ":
            pass
        else:
            sortedList = sortedSearch(sortedList, wordLow, assignInt, compInt)
                                                                               #https://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/ for help with sorting and printing

print("\n\n\n")

for i in range(len(sortedList)):
    print(sortedList[i].word, sortedList[i].val)

print("\n\n\nThe number of unique words is: ")
print(len(sortedList))
print("\n")


print("\n\n\n")
print("The first 10 words are: ")
#n_items = takeFirst(10, d_w_unsorted.items())
for i in range(0,11):
    print(sortedList[i].word, sortedList[i].val)
print("\n\n")
listLenMin10 = len(sortedList) - 10
print("The last 10 words are: ")

for i in range(listLenMin10,len(sortedList)):
    print(sortedList[i].word, sortedList[i].val)
print("\n\n")

print("The number of comparisons is: " + str(compInt.total))
print("The number of assignments is: " + str(assignInt.total))


print("Process time = ")
print(time.time() - start_time)
print("\n")
