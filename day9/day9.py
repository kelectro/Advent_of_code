from itertools import combinations
filepath = '/home/kiagkons/Desktop/advent of code/day9/day9.in'

#load all values in a list of int
def load_commands(path):
    commands = [int(cmd.strip()) for cmd in open(path,'r')]
    return(commands)

#part1 
def check_sequence(commands,premable_size):
    terminated = False
    i = 0
    res = []

    while i< len(commands) and terminated == False:
        #get all possible combinations
        cmb = list(combinations(commands[i:i+premable_size],2))
        #sum values
        res = list(map(sum,cmb))
        #bruteforce check
        if commands[premable_size+i] in res:
            i +=1
            res = []
        else :
            #return the number 
            return(commands[premable_size+i])
            break

def get_weakness(commands,goal):
    # goal =  15353384
    index = 0
    sum_val = 0
    j = 0
    keep = []
    terminated = False

    while terminated == False:
        #if we need more to reach goal, add and keep the values
        if sum_val < goal :
            sum_val += commands[index]
            keep.append(commands[index])
            index +=1            
        if sum_val == goal :
            #we reached succesfully the goal 
            return(min(keep)+max(keep))
        elif sum_val > goal :
            # in this case we need to start over but shifting the index one postition to the right
            # since we are looking for consecutive numbers.
            # clean everything            
            keep = []
            sum_val = 0
            #increse index 
            j +=1
            index = j




prem_size = 25
commands = load_commands(filepath)
result = check_sequence(commands,prem_size)
print('The number that does not have the property is :',result )
encryption_weakness = get_weakness(commands,result)
print('The encryption weakness is:',encryption_weakness)
