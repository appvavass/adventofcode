import pandas as pd

#this function perform the tasks given in the puzzle
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

#create datasets from input    
instructions = pd.read_csv('input.txt', sep=' ', header = None, names=('operation','value'))
instructions['ex_counter'] = 1

#create initial references
startline = 0
accumulator = 0
it = 0

#this function iterates the instructions to get the accumulator value before the infinite loop
def run_sol(df):
    startline = 0
    accumulator = 0
    it = 0
    savepos = []
    while True:
        savepos.append(startline)
        old_acc = accumulator
        operation, val_to_add, ex_count = df.iloc[startline]
        ex_count += 1
        df.loc[startline,'ex_counter'] = ex_count
        new_acc, newline = executor(startline, operation,accumulator,val_to_add)
        it = it + 1
        startline = newline
        accumulator = new_acc
        if newline in savepos: 
            fail = True
            #print('new line should be:',newline)
            savepos.reverse()
            lastpos = savepos[0]
            break
        if newline == (len(df)): 
            fail = False
            lastpos = None
            print('success')
            break
    return old_acc, fail, lastpos

#run the first part
answer,fail,failpos = run_sol(instructions)
print('sol part 1:',answer, 'failed?', fail)


#function to modify the puzzle with jmp or nop
def inst_changer(original):
    if original == 'jmp': 
        #print('function input:', original)
        return 'nop'
    elif original == 'nop': 
        #print('function input:', original)
        return 'jmp'
    else: return original

counter = 0
line = 0

while True:
    if counter > 1:
        del instructions
        instructions = bckp.copy(deep = True)
    correction = inst_changer(instructions.loc[line,'operation'])
    bckp = instructions.copy(deep=True)
    instructions.at[line,'operation'] = correction
    answer,fail,failpos = run_sol(instructions)
    
    line += 1
    counter += 1
    if fail == False: 
        print('sol part 2:',answer, 'failed?', fail)
        break
    elif counter > len(instructions):
        print('2 many lines processed')
        break
    else:
        continue
        

    
