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

class Hash_Table_Words:
    def __init__(self,size):
        self.hash_table = [{} for i in range(size) ]  #create empty hash table
    def insertAndSearch(self, key, _wordC):
        hash_index = hashing_val(self, key)
    #    print(hash_index)
        for k,v in self.hash_table[hash_index].items():          #for each value within the dictionary at the index of the hash tab
            if key == k:
                self.hash_table[hash_index].update({key : (v+1)})
                return
        _wordC.add(1)
        self.hash_table[hash_index].update({key : 1})   #else add new key
        #print(self.hash_table[hash_index])
    def search(self, key):
        hash_index = hashing_val(self, key)
        for k,v in self.hash_table[hash_index].items():
            if key == k:
                print(k,v)


my_hash_t = Hash_Table_Words(50000)
print(my_hash_t.hash_table)

print(len(my_hash_t.hash_table))

wordC = wordCounter()

filename = "wordlist.txt"
f = open(filename, 'r')


for line in f:
    line = line.translate(str.maketrans('','', '!.@"$?&:;,/()*^%>+=|<}{[]'))   #remove punctuation from input sequence  https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
    line = re.sub('[0-9]', '', line)                               #remove numbers https://stackoverflow.com/questions/35256946/python-3x-remove-numbers-from-file-names
    for word in line.split():
        wordLow = word.lower()      #set word to lower case
        wordLow = wordLow.replace(wordLow, "") if wordLow.startswith("'") else wordLow
        if wordLow != '':
            my_hash_t.insertAndSearch(wordLow, wordC)

print(my_hash_t.hash_table)

print(my_hash_t.search('a'))
print(wordC.total)
