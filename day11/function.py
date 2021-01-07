def seatchecker(row,col,status,df):
    checklist = [-1,0,1]
    busy = 0
    target_seat = df[row][col]

    for a in checklist:
        for b in checklist:
            check_row = row + a
            check_col = col + b
            if a == 0 and b == 0: continue
            try:
                seat_status  = df[checkrow][check_col]
                if seat_status == '#': busy += 1
            except:
                seat_status = '.'
    
    if target_seat == 'L' and busy == 0:
        return '#'
    elif target_seat == '#' and busy > 3:
        return 'L'
    else:
        return target_seat
