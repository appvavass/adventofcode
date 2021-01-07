import copy
fhandler  = open('tes2.txt')
df = []

for row in fhandler:
    line = []
    row = row.rstrip('\n')
    for letter in row:
        line.append(letter)
    df.append(line)
####################### pre-processing done

def sorround(row,col,dataf):
    adjacent = [-1,0,1]
    summasummarum = 0
    line = []
    maps = []
    for a in adjacent:
        for b in adjacent:
            row_pos = row + a
            col_pos = col + b
            try:
                seat = dataf[row_pos][col_pos]
            except: seat = '.'
            if seat == '#':
                seat_symbol = 1
            else: seat_symbol = 0
            line.append(seat_symbol)
            if b == 1:
                maps.append(line)
                summasummarum += sum(line)
                line = []
    return maps, summasummarum



def seatchecker(row,col,dataf):
    checklist = [-1,0,1]
    busy = 0
    target_seat = dataf[row][col]

    for a in checklist:
        for b in checklist:
            seat_status = None
            check_row = row + a
            check_col = col + b
            if a == 0 and b == 0: continue
            try:
                seat_status = dataf[check_row][check_col]
                if seat_status == '#': 
                    busy += 1
                else: continue
            except:
                seat_status = '.'
    #print('seat {},{} has {} occupied seats'.format(row,col,busy))
    
    if target_seat == 'L' and busy == 0:
        return '#'
    elif target_seat == '#' and busy > 3:
        return 'L'
    else:
        return target_seat

it = 0
while True:
    new_df = copy.deepcopy(df)

    for r in range(len(df)):
        for c in range(len(df[0])):
            maps,summaps = sorround(r,c,df)
            print(maps,summaps)
            new_df[r][c] = seatchecker(r,c,df)
            #print(df)
            #print(new_df)
            #input('enter')
    occ = 0
    cont = False
    for r in range(len(df)):
        for c in range(len(line)):
            if df[r][c] == '#': occ += 1
            if df[r][c] != new_df[r][c]:
                cont =  True
    df = copy.deepcopy(new_df)
    it += 1

    if cont == False: break

print('answer:', occ)
print('iterations',it)