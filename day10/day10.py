filepath = '/home/kiagkons/Desktop/advent of code/day10/sample.in'

def load_data(path):
    data = [int(x) for x in open(path,'r')]
    return(data)

def jolt_distribution(adapters):
    is_one = 0
    is_two = 0
    is_three = 0
    plug_voltage = 0

    adapters.sort()
    adapters.append(adapters[-1]+3)

    

    for j in adapters:
        if j == plug_voltage +1:
            is_one +=1
            plug_voltage = j
        elif j == plug_voltage +2:
            is_two +=1
            plug_voltage =j
        elif j == plug_voltage +3 :
            is_three +=1
            plug_voltage = j
    
    return(is_one*is_three)



def task2(adapters):
    #add the zero element
    adapters.append(0)
    adapters.sort()
    #append the max +3
    adapters.append(adapters[-1]+3)

    paths = [0]*(max(adapters) +1)
    
    paths[0] = 1
    # print(paths)

    for index in range(1,max(adapters)+1):
        # print(index)
        for x in range(1,4):
            print('index :{}, x:{}'.format(index,x))
            if (index - x) in adapters :
                paths[index] += paths[index - x]
                print(paths[index])
    
    print(paths[-1])




# task1 = jolt_distribution(load_data(filepath))
task2(load_data(filepath))

    
# print('Taks 1 ', task1)