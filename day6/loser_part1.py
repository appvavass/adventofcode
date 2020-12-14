inp_fil = open('input.txt')

big_ans = []
group_ans = []

for line in inp_fil:
    line = line.rstrip('\n')
    if line == '':
        big_ans.append('void')
    else:
        big_ans.append(line)
ans = ''
for el in big_ans:
    if el != 'void':
        ans = ans + el
    else:
        group_ans.append(ans)
        ans = ''

total_yes = 0

#print(group_ans)

for e in group_ans:
    comparator = []
    for letter in e:
        #print('checking letter', letter)
        if letter not in comparator:
            comparator.append(letter)
        else: continue
    #print(comparator)
    score = len(comparator)
    total_yes = total_yes + score

print('sum of yes ansers is {}'.format(total_yes))



