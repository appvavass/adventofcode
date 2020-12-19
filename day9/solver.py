fopen = open('input.txt')
cluster = 25
puzzle = []
for i in fopen:
    i.rstrip('\n')
    puzzle.append(int(i))
print(puzzle)