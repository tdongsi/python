'''
Created on May 6, 2014

@author: tdongsi
'''

'''
Solve puzzle: from a source word, modify one character in each step such that the new word is valid in order to get to destination word

Example:
('mold -> mole', 'mole -> male', 'male -> mace', 'mace -> mach', 'mach -> each', 'each -> etch')
'''

def addWord(d, length, w):
    if len(w) == length:
        d.add(w)

def getDict(dict, length):
    fin = open('../data/words.txt')

    for line in fin:
        l = line.strip()
        addWord(dict, length, l)

lookup = set()
fullPath = {}
wordList = []
found = set()

def findValidChange(w, i, path):
    # print("Find valid change", w, i)
    l = list(w)
    for c in range(ord('a'), ord('z') + 1):
        l[i] = chr(c)
        w2 = ''.join(l)
        if w2 in lookup:
            p = path + (("%s -> %s" % (w, w2)),)
            if (w2 not in found):
                wordList.append(w2)
                found.add(w2)
                fullPath[w2] = p

def findPair(w, path):
    for i in range(len(w)):
        findValidChange(w, i, path)


def solvePuzzle(src, dest):
    assert len(src) == len(dest)

    getDict(lookup, len(src))

    wordList.append(src)
    findPair(src, tuple())
    found.add(wordList.pop(0))

    while dest not in found:
        if len(wordList) == 0:
            print('Cannot find a path: ', len(found), found)
            return
        w = wordList[0]
        findPair(w, fullPath[w])
        found.add(wordList.pop(0))

    print(fullPath[dest])


if __name__ == '__main__': 
#     solvePuzzle('mold', 'etch')
    solvePuzzle('hello', 'class')
#     solvePuzzle('accent', 'sprint')


