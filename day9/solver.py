fopen = open('input.txt')
cluster = 25
puzzle = []
for i in fopen:
    i.rstrip('\n')
    puzzle.append(int(i))

it  = 0
for i in range(0,len(puzzle)):
    check = False
    index = i 
    number = puzzle[index]
    start = i - cluster
    finish = i
    if i < cluster: continue
    to_search = puzzle[start:finish]
    #print(to_search, number)
    for k in to_search:
        for v in to_search:
            #print(k,v,number)
            if k == v: continue 
            if (k+v) == number and k != v:
                #print('found match {} {}'.format(k,v))
                check = True
    if check == False:
        print('solution part 1: {}'.format(number))
        new_puzzle = puzzle[:i]
        break

def cont_finder(set_len, sets, target):
    for i in range(0,len(sets)):
        start = i - set_len
        finish = i
        if i < set_len: continue
        interval = sets[start:finish]
        #print(interval)
        if sum(interval) == target:
            return interval


for i in range(2,len(new_puzzle)):
    lst = cont_finder(i, new_puzzle, number)
    if lst != None: 
        #print(lst)
        break

a = min(lst)
b = max(lst)
answer = a + b
print('solution part 2:', answer)
    
