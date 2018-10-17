#Header file for SelectionSort.py
#Written by Kenneth Maguire
import matplotlib
import matplotlib.pyplot as plt

class comparisonCounter:
    total = 0
    def __init__(self):
        self.total = 0
    def add(self, x):
        self.total += x

class exchangeCounter:
    total = 0
    def __init__(self):
        self.total = 0
    def add(self, x):
        self.total += x
class nCounter:
    total = 0
    def __init__(self):
        self.total = 0
    def add(self, x):
        self.total += x

class plotCandE:
    exchY = []
    compY = []
    countX = []
    def __init__(self):
        self.exchY = []
        self.compY = []
        self.countX = []


def comparisonAndCountSS(_unsortedArray, _min, _i, _comp):
    _comp.add(1)
    if(_unsortedArray[_i] < _unsortedArray[_min]):
        return True
    else:
        return False

def comparisonAndCountQS(_partArray, _j, _pivot, _comp):
    _comp.add(1)
    if(_partArray[_j].word <= _pivot.word ):
        return True
    else:
        return False


def plotCompAndExchange(_count, _exchange, _comparison, _plotArrays):
    def appendValues():
        _plotArrays.countX.append(_count)
        _plotArrays.exchY.append(_exchange)
        _plotArrays.compY.append(_comparison)
    if _count == 1:
        appendValues()
    elif _count == 10:
        appendValues()
    elif _count == 100:
        appendValues()
    elif _count == 1000:
        appendValues()
    elif _count == 10000:
        appendValues()
    elif _count == 100000:
        appendValues()
    elif _count == 1000000:
        appendValues()




def inputFile(_fileNum):
    path = 'data/'
    txtIndex = ['duplicate.txt', 'nearly-sorted.txt', 'nearly-unsorted.txt', 'one-million-randoms.txt', 'shuffled.txt', 'sorted.txt', 'unsorted.txt']
    #passedList = [1,3,7,8,3,5,6,7,10000,12, 14, 300,1, 1,2,12, 100, 1200, 145,1]
    f = open(path + txtIndex[_fileNum], 'r')

    #print(txtFileSelection.read())
    #next(txtFileSelection)
    passedList = []
    with f:
        next(f)         #skip header
        for line in f:
            line = line.strip()
            passedList.append(int(line))
    f.close()
    return passedList
