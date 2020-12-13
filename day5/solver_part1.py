def locator(string, type):
    print('checking for', type)
    if type == 'row':
        row_end = 127
    else:
        row_end = 7
    row_start = 0
    for e in string:
        midpoint = int((row_end-row_start)/2)
        if e == 'B' or e == 'R':
            row_start = midpoint
            print('new row_start:', midpoint)
        else:
            row_end = row_start -1 + midpoint
            print('new row_end:', midpoint)
    return row_end

fhandler = open('input.txt')
seat_ID_list = []
seat_ID_list_t = []

# for line in fhandler:
#     seat = line.rstrip('\n')
#     row = seat[:7]
#     col = seat[7:]
#     rnum = locator(row, 'row')
#     cnum = locator(col,'col')
#     print('row nr:', rnum)
#     print('col nr:', cnum)
#     seat_ID = rnum*8 + cnum
#     print('ID:', seat_ID)
#     seat_ID_list.append(seat_ID)

# print('maximum seat ID {}'.format(max(seat_ID_list)))

test1 = 'BFFFBBFRRR'
test2 = 'FFFBBBFRRR'
test3 = 'BBFFBBFRLL'

test = [test1, test2, test3]

print('========TEST AREA========')
for line in test:
    seat = line.rstrip('\n')
    row = seat[:7]
    print('row ID:', row)
    col = seat[7:]
    print('col ID:', col)
    rnum = locator(row, 'row')
    cnum = locator(col,'col')
    print('row nr:', rnum)
    print('col nr:', cnum)
    seat_IDt = rnum*8 + cnum
    print('ID:', seat_IDt)
    seat_ID_list_t.append(seat_IDt)
    input('enter .-.....')
    

print('maximum TEST seat ID {}'.format(max(seat_ID_list_t)))

