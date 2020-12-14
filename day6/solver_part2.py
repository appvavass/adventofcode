inp_fil = open('input.txt')

big_ans = []
group_ans = []

for line in inp_fil:
    line = line.rstrip('\n')
    if line == '':
        big_ans.append('void')
    else:
        big_ans.append(line)

#print(big_ans)
participant_number = 0
ans_dict = {}

for el in big_ans:

    if el == 'void':
        group_ans.append(ans_dict)
        ans_dict = {}
        
    else:   
        for letter in el:
            ans_dict[letter] = ans_dict.get(letter, 0) + 1
        ans_dict['participants'] = ans_dict.get('participants', 0) + 1
        
#print(group_ans)
ans_list = []

for dictionary in group_ans:
    yes_to_all = 0
    participant = dictionary.get('participants')
    for k in dictionary:
        val = dictionary.get(k)
        if k == 'participants': continue
        #print('DEBUG', val, k)
        if val == participant:
            yes_to_all += 1
        else: continue
    ans_list.append(yes_to_all)
    #print('yes to all: {}'.format(yes_to_all))
    #print('DEBUG--- New dictionary')

total =  sum(ans_list)
print('your answer is',total)
    







