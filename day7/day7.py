import re
from collections import defaultdict




def load_data(path):
    file = open(path,'r')
    data = file.readlines()
    file.close()
    # print(len(data))
    return(data)




def parse_data(data):

    p = 0
    # luggage_policy= {}
    # A nested dict has been created with the following structure ({parent:{child1:amount, child2:amount}})
    lug_dict = defaultdict(dict)

    parent_pattern = re.compile("(\A\w+\s\w+)")
    child_pattern = re.compile("(\d\s\w+\s\w+)")

    for bag in data:
        parent_bag = re.findall(parent_pattern,bag)
        child_bags = re.findall(child_pattern,bag)

        for substring in child_bags:
            p +=1
            amount = re.match('\d',substring).group()
            lug_type = re.findall('[a-zA-Z]+\s[a-zA-Z]+',substring)
            lug_dict[parent_bag[0]][lug_type[0]] = amount
    return(lug_dict)


def breadth_first(policy_dict):

    answer = set()   
                    
    q = ['shiny gold']                  # Work queue for traversing bags
    while len(q) != 0:
        current = q.pop(0)
        for key in policy_dict.keys():
            print(key)
            if key in answer:             # Skip if already counted.
                continue
            if current in policy_dict[key]:      # If bag contains current-bag,
                q.append(key)             # add to queue and answer
                answer.add(key)

    return(len(answer))







filepath = '/home/kiagkons/Desktop/advent of code/day7/sample.in'

data = load_data(filepath)
dict = parse_data(data)
result = breadth_first(dict)
print('The number of luggages is ',result)

