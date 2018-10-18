"""
Kenneth Maguire
Python 3 Program


SearchHash.py
This program add the works of shakespeare to a hash table and determines how many of each word exists
The program does this through an hash table searching method.




"""


import string
import time
import random
from itertools import islice
import re

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

class wordCounter:
    total = 0
    def __init__(self):
        self.total = 0
    def add(self, x):
        self.total += x

def hashing_val(_hash_table, key):
    #random.seed()
    #randNum = random.randint(50000,51000)
    #print(randNum)
    asciiKey = 0
    for char in key:
        asciiKey += ord(char)
    hashSeed = asciiKey * 54001
    return (hashSeed % 58243) % len(_hash_table.hash_table) #58243 is a prime number using g(x) = (kx mod p) mod n https://en.wikipedia.org/wiki/Perfect_hash_function#Minimal_perfect_hash_function
def getListFromHash(_hash_table, _unsortedList):
    for i in range(len(_hash_table.hash_table)):
        for k,v in _hash_table.hash_table[i].items():
            if k == "":
                pass
            else:
                _unsortedList.append((k,v))
    return _unsortedList

class Hash_Table_Words:
    def __init__(self,size):
        self.hash_table = [{} for i in range(size) ]                        #create empty hash table
    def insertAndSearch(self, key, _wordC, _comp, _assign):
        hash_index = hashing_val(self, key)                                 #get hash index
    #    print(hash_index)
        for k,v in self.hash_table[hash_index].items():                     #for each value within the dictionary at the index of the hash tab
            _comp.add(1)       #add 1 to comp
            if key == k:
                self.hash_table[hash_index].update({key : (v+1)})           #if key found, add one to occurrences and return
                return
        _wordC.add(1)
        _assign.add(1)
        self.hash_table[hash_index].update({key : 1})                       #else add new key with occurence = 1, add 1 to unique word count, and 1 to assign





start_time = time.time()

# start driver code
my_hash_t = Hash_Table_Words(50000)
print(my_hash_t.hash_table)

print(len(my_hash_t.hash_table))
compInt = comparisonCounter()
assignInt = assignmentCounter()
wordC = wordCounter()

filename = "wordlist.txt"
f = open(filename, 'r')


for line in f:
    line = line.translate(str.maketrans('','', '!.@"$?&:;,/()*^%>+=|<}{[]'))   #remove punctuation from input sequence  https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
    line = re.sub('[0-9]', '', line)                               #remove numbers https://stackoverflow.com/questions/35256946/python-3x-remove-numbers-from-file-names
    for word in line.split():
        wordLow = word.lower()      #set word to lower case
        wordLow = wordLow.replace(wordLow, "") if wordLow.startswith("'") else wordLow      #remove words starting with '
        if wordLow != '':
            my_hash_t.insertAndSearch(wordLow, wordC, compInt, assignInt)



unsortedList = []
unsortedList = getListFromHash(my_hash_t, unsortedList)
sortedList = sorted(unsortedList)



print(my_hash_t.hash_table)
print(sortedList)
#print(my_hash_t.search('a'))

print("\n\n\nThe number of unique words is: ")
print(wordC.total)


print("The first 10 words are: ")
for k,v in sortedList[0:10]:
    print(k,v)
print("\n\n")
listLenMin10 = len(sortedList) - 10
print("The last 10 words are: ")
#n_items = takeLast(listLenMin10, d_w_unsorted.items())
for k,v in sortedList[listLenMin10:len(sortedList)]:
    print(k,v)
print("\n\n")

print("Process time = ")
print(time.time() - start_time)
print("\n")


print("The number of comparisons is: " + str(compInt.total))
print("The number of assignments is: " + str(assignInt.total))
