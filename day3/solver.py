import pandas as pd
import numpy as np

init =  open('input.txt')
countrow = 0
countcol = 0

for row in init:
    countrow += 1
    if countrow == 1:
        for letter in row:
            countcol += 1

limit = 32*7
countcol = countcol - 1
countcol = countcol * limit
print('rows: {}, cols: {}'.format(countrow,countcol))
df = np.zeros((countrow,countcol))

def assigner(string):
    if string == '#':
        return 1
    else: return 0
    
    
rowindex = 0
init2 = open('input.txt')

for row in init2:
    row = row.rstrip('\n')
    colindex = 0
    x = 0
    while x < limit:
        for letter in row:
        #print('calling function on character: {}'.format(letter))
            df[(rowindex,colindex)] = assigner(letter)
            colindex += 1
        x += 1
    rowindex += 1

print(df)

sloperes = []
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]

for test in slopes:
    startposX = 0
    startposY = 0
    treecount = 0
    while startposX < 323:
        treecheck = df[startposX,startposY]
        if treecheck == 1: 
            treecount += 1
        startposX += test[1]
        startposY += test[0]
    sloperes.append(treecount)
print(sloperes)
#print('total trees encountered:{}'.format(treecount))

for e in sloperes:
    if e == sloperes[0]: product = e
    else: product = e*product

print(product)