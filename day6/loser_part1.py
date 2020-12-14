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

print(group_ans[:4])




