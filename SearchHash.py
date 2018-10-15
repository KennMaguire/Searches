
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
    return (len(key) * 181) % len(_hash_table.hash_table)

class Hash_Table_Words:
    def __init__(self,size):
        self.hash_table = [[] for i in range(size) ]
    def insert(self, key):
        hash_index = hashing_val(self, key)
        print(hash_index)
        self.hash_table[hash_index].append(key)
        print(self.hash_table[hash_index])



my_hash_t = Hash_Table_Words(25000)
print(my_hash_t.hash_table)

print(len(my_hash_t.hash_table))
testVal = 'potato'

my_hash_t.insert(testVal)
my_hash_t.insert(testVal)
my_hash_t.insert(testVal)
my_hash_t.insert(testVal)

print(my_hash_t.hash_table)
