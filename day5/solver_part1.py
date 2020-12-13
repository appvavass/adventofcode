def locator(string, type):
    if type == 'row':
        row_end = 127
    else:
        row_end = 7
    row_start = 0
    for e in string:
        midpoint = int(row_end/2)
        if e == 'B':
            row_start = midpoint
        else:
            row_end = midpoint
    return row_end

fhandler = open('input.txt')
seat_ID_list = []

for line in fhandler:
    seat = line.rstrip('\n')
    row = seat[:7]
    col = seat[7:]
    rnum = locator(row, 'row')
    cnum = locator(col,'col')
    print('row nr:', rnum)
    print('col nr:', cnum)
    seat_ID = rnum*8 + cnum
    seat_ID_list.append(seat_ID)

print('maximum seat ID {}'.format(max(seat_ID_list)))
