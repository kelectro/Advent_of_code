
filename = '/home/kiagkons/Desktop/advent of code/day3/map.txt'

def load_data(path):
    load = open(filename,'r')
    game_map = []
    for line in load :
        data_row = list(line.strip())
        game_map.append(data_row)
    load.close()
    
    return game_map

def create_map(game_map,step_x,step_y):
    trees = 0
    max_x = len(game_map[0])
    max_y = len(game_map)
 
    index = [(x * step_y % max_y, (x * step_x) % max_x) for x in range(0, max_y // step_y)]
    print(index)
    for i,j in index :
        if game_map[i][j] == '#':
            trees +=1
    
    return(trees)
    

    

game_map =load_data(filename)
#Task 1
puzzle_1 =(create_map(game_map,step_x = 3, step_y= 2))
print('The number of trees in puzzle 1 is', puzzle_1)


'''
Task 2

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.

'''

# Task 2

puzzle_2_1 =(create_map(game_map,step_x = 1, step_y= 1))
puzzle_2_2 =(create_map(game_map,step_x = 3, step_y= 1))
puzzle_2_3 =(create_map(game_map,step_x = 5, step_y= 1))
puzzle_2_4 =(create_map(game_map,step_x = 7, step_y= 1))
puzzle_2_5 =(create_map(game_map,step_x = 1, step_y= 2))

result = puzzle_2_1*puzzle_2_2*puzzle_2_3*puzzle_2_4*puzzle_2_5
print('The total number of trees is : ',result)

