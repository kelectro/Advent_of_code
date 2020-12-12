import copy
filepath = '/home/kiagkons/Desktop/advent of code/day8/day8.in'

def load_data(path):
    file = open(filepath,'r')
    data = file.readlines()
    file.close()
    data = [data.strip() for data in data ]
    data = [data.split() for data in data]
    # print(data[1][0])
    # print(data)
    return(data)



def compiler(data):
    terminated = False
    command = []
    qunatity = []
    visited = []
    accumulator = 0
    i=0
    
    for cmds in data:
        # print(cmds[0])
        command.append(cmds[0])
        qunatity.append(cmds[1:])
    # print(len(command))
    

    # for i in range(len(command)):
        # print(i)

    while i not in visited and terminated == False  :    
        print('i =',i)
        print('command',command[i])
        visited.append(i)
        if command[i] == 'nop':
            i +=1
            pass
        elif command[i] == 'acc':
            accumulator += int(qunatity[i][0])
            i +=1
        elif command[i] == 'jmp':
            i += int(qunatity[i][0])
            # print(i)
        if i == len(data):
            print('Terminated')
            terminated = True
    return(terminated,accumulator)

    # print(accumulator)


def part2(instructions):
    # print(data)
    new_data =[]

    for i in range(len(instructions)):
        if instructions[i][0] == 'nop':
            instructions[i][0] = 'jmp'
        # compiler(instructions)
        elif instructions[i][0] == 'jmp':
            instructions[i][0] = 'nop'
        compiler(instructions)
        
def part2b(instructions):
    new_instructions = copy.deepcopy(instructions)
    terminated = False
    index = 0
    # print(new_instructions[10][0])
    
    while terminated == False : 
        print('2b index',index)       
        if new_instructions[index][0] == 'nop':
            new_instructions[index][0] = 'jmp'
        elif new_instructions[index][0] == 'jmp':
            new_instructions[index][0] = 'nop'
        terminated,result = compiler(new_instructions)
        # print('\n',new_instructions)
        new_instructions = copy.deepcopy(instructions)
        index +=1
    print('Terminated result',result)

        
# compiler(load_data(filepath))
part2b(load_data(filepath))