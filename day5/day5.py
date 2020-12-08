filepath = '/home/kiagkons/Desktop/advent of code/day5/data.txt'


def ticket_decode(ticket):
    high = 128
    low = 0

    left = 0
    right = 8
    for char in ticket :
        if char == 'F':
            dif = (high-low)/2
            high = high - dif
        if char == 'B' :
            dif = (high-low)/2
            low = low + dif
        if char == 'L':
            val = (right-left)/2
            right = right - val
        if char == 'R':
            val = (right-left)/2
            left = left + val
    # print(high-1)
    # print(left)
    seat_id = ((high-1) * 8 )+ left
    # print('id',seat_id)
    return(seat_id)




def load_data(path):
    file = open(path,'r')
    data = file.readlines()
    file.close()    
    data = [data.strip() for data in data]
    return(data)


tickets = load_data(filepath)
seat_ids = [ticket_decode(ticket) for ticket in tickets]
print(max(seat_ids))
