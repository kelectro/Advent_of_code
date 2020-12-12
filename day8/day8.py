import copy
filepath = '/home/kiagkons/Desktop/advent of code/day8/day8.in'


#load the data in lists. every list has ['command', 'quantity']
def load_data(path):
    file = open(filepath,'r')
    data = file.readlines()
    file.close()
    data = [data.strip() for data in data ]
    data = [data.split() for data in data]
    return(data)



def compiler(data):
    terminated = False
    command = []
    qunatity = []
    visited = []
    accumulator = 0
    i=0

    #assign command and quantity to different values to make it easir to work with
    for cmds in data:
        command.append(cmds[0])
        qunatity.append(cmds[1:])

    while i not in visited and terminated == False  :    
        #keep track of visited commands
        visited.append(i)

        if command[i] == 'nop':
            i +=1
            pass
        elif command[i] == 'acc':
            accumulator += int(qunatity[i][0])
            i +=1
        elif command[i] == 'jmp':
            i += int(qunatity[i][0])

        if i == len(data):
            # we reached the end of file
            terminated = True
        
        if i > len(data):
            raise  ValueError("List index exhaustion, no possible solution")

    return(terminated,accumulator)



        
def part2(instructions):
    #save original commands
    new_instructions = copy.deepcopy(instructions)
    terminated = False
    index = 0
    
    while terminated == False : 
        if new_instructions[index][0] == 'nop':
            new_instructions[index][0] = 'jmp'
        elif new_instructions[index][0] == 'jmp':
            new_instructions[index][0] = 'nop'
        terminated,result = compiler(new_instructions)
        #replace modded list with original in order to try next possible jmp<-->nop switch
        new_instructions = copy.deepcopy(instructions)
        index +=1
    return(result)

        
acc1 = compiler(load_data(filepath))
print('Last known value for accumulator before the infinite loop was : ',acc1[1])
result = part2(load_data(filepath))
print('The program has safely terminated. Last accumulator value is: ', result)