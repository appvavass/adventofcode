f = open('input.txt')
chargers = []
for e in f:
    e = e.rstrip('\n')
    e = int(e)
    chargers.append(e)
    
start_r = 0
conversions = []
while True:
    valid_charger = []
    r_min = start_r + 1
    r_max = start_r + 3
    for e in chargers:
        if e >= r_min and e <= r_max:
            valid_charger.append(e)
    least_valid = min(valid_charger)
    chargers.remove(least_valid)
    jump  = least_valid - start_r
    conversions.append(jump)
    start_r =  least_valid
    if chargers == []: break

jmp_1 = []
jmp_3 = [3] ### including the inbuilt charger
for e in conversions:
    if e == 1:
        jmp_1.append(e)
    elif e == 3:
        jmp_3.append(e)
    else: continue

print('{} jumps of 1, and {} jumps of 3'.format(len(jmp_1),len(jmp_3))) 
answer = len(jmp_1)*len(jmp_3)  
print('answer part 1:', answer)     
print(conversions)