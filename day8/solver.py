import pandas as pd

def executor(line, operation, acc, inval): #position, operation, starting_accumulator, instruction_value
    if operation == 'acc':
        newline = line + 1
        return acc + inval, newline
    elif operation == 'nop':
        newline = line + 1
        return acc, newline
    elif operation == 'jmp':
        newline = line + inval
        return acc, newline
    
instructions = pd.read_csv('input.txt', sep=' ', header = None, names=('operation','value'))

instructions['ex_counter'] = 1

print(instructions.iloc[0])


startline = 0
accumulator = 0
it = 0

while True:
    operation, val_to_add, ex_count = instructions.iloc[startline]
    new_acc, newline = executor(startline, operation,accumulator,val_to_add)
    it = it + 1
    startline = newline
    accumulator = new_acc
    if it == 2: break
