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

def hashing_val(_hash_table, key):
    random.seed()
    randNum = random.randint(1,10)
    hashSeed = len(key) * randNum
    return (hashSeed * randNum * 181) % len(_hash_table.hash_table)

class Hash_Table_Words:
    def __init__(self,size):
        self.hash_table = [{} for i in range(size) ]  #create empty hash table
    def insertAndSearch(self, key):
        hash_index = hashing_val(self, key)
    #    print(hash_index)
        for k,v in self.hash_table[hash_index].items():          #for each value within the dictionary at the index of the hash tab
            if key == k:
                self.hash_table[hash_index].update({key : (v+1)})
                break
        else:
            self.hash_table[hash_index].update({key : 1})
        #print(self.hash_table[hash_index])
    def search(self, key):
        hash_index = hashing_val(self, key)


my_hash_t = Hash_Table_Words(25000)
print(my_hash_t.hash_table)

print(len(my_hash_t.hash_table))

"""
testVal = 'potato'
my_hash_t.insertAndSearch(testVal)
my_hash_t.insertAndSearch(testVal)
my_hash_t.insertAndSearch(testVal)
my_hash_t.insertAndSearch(testVal)


testVal = 'potata'



my_hash_t.insertAndSearch(testVal)
my_hash_t.insertAndSearch(testVal)
my_hash_t.insertAndSearch(testVal)
"""

filename = "wordlist.txt"
f = open(filename, 'r')


for line in f:
    line = line.translate(str.maketrans('','', '!.@"$?&:;,/()*^%>+=|<}{[]'))   #remove punctuation from input sequence  https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
    line = re.sub('[0-9]', '', line)                               #remove numbers https://stackoverflow.com/questions/35256946/python-3x-remove-numbers-from-file-names
    for word in line.split():
        wordLow = word.lower()      #set word to lower case
        wordLow = wordLow.replace(wordLow, "") if wordLow.startswith("'") else wordLow
        my_hash_t.insertAndSearch(wordLow)

print(my_hash_t.hash_table)
