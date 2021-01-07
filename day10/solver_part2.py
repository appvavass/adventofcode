f = open('test2.txt')
converters = []
for e in f:
    e = e.rstrip('\n')
    e = int(e)
    converters.append(e)

start = [0]
sequence = []
end = max(converters)

def findnext(input_l, starts, input_so_far):
    possible  = []
    jmp_range = [1,2,3]
    for i in jmp_range:
        for start in starts:
            end = start + i
            if end in input_l:
                possible.append(end)
                input_so_far.append(end)
                return findnext(input_l, possible, input_so_far)
    return end, input_so_far
            
a,long_seq = findnext(converters, start, sequence)
long_seq.insert(0,0)
last = long_seq[len(long_seq)-1]
last = last + 3
long_seq.append(last)
print('answer part1',long_seq)
#long_seq.sort(reverse = True)

sol = []
for el in long_seq:
    pot_ways = 0
    for i in [1,2,3]:
        if el == 0:
            if (el+i) in long_seq:
                pot_ways += 1
        else:
            if (el - i) in long_seq:
                pot_ways += 1
    if pot_ways == 0: continue
    app = (el, pot_ways)
    sol.append(app)

sol.sort()    
print(sol)

def child(tuple):
    return tuple[1]
def key(tuple):
    return tuple[0]

def tribonacci(k):
    if k > 3:
        return tribonacci(k-1) + tribonacci(k-2) + tribonacci(k-3)
    else:
        return k 


def fibonacci(k):
    if k > 2:
        return fibonacci(k-1) + fibonacci(k-2) 
    else:
        return k 


parent = 1
final_sol = []
for i in range(len(sol)):
    val = sol[i]
    k = key(val)
    c = child(val)
    final_sol.append(c)

print(final_sol)







