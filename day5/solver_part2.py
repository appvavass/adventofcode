fhandler = open('seat_list.txt')

seat_list = []

for row in fhandler:
    ID = row.rstrip('\n')
    ID = int(ID)
    seat_list.append(ID)

seat_list.sort()
#print(seat_list)

it = 0
for e in seat_list:
    if e == seat_list[0]: continue
    prev_seat = seat_list[it]
    pos = it + 2
    next_seat = seat_list[pos]

    diff_prev = e - prev_seat
    diff_next = next_seat - e
    it += 1

    if diff_prev != 1:
        yourseat = e - 1
        print('Your seat is {}'.format(yourseat))
        break
