seat = 'BBFFBFFRRR'

row = seat[:7]
col = seat[7:]
##Converting input into mathematical good stuff

row_lst = []
col_lst = []
for e in row:
    if e == 'B':
        row_lst.append(1)
    else:
        row_lst.append(-1)

for e in col:
    if e == 'L':
        col_lst.append(1)
    else:
        col_lst.append(-1)

print(row_lst)
print(col_lst)

def row_locator(lst):
    start_row = 127
    for e in lst:
        new_row = start_row + start_row/2  