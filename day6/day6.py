import numpy as np
filename = '/home/kiagkons/Desktop/advent of code/day6/day6.in'


def parse_data(filename):

    file = open(filename)
    data = file.read()
    file.close()
    data = data.split('\n\n')
    data_merged= [data.replace('\n', ' ') for data in data]
    data = [data.split() for data in data_merged]
    return(data,data_merged)

def ans_counts(data):
    d = []
    j=0

    for string in data:
        for letter in string:
            for l in letter:
                d.append(l)
        j += len(np.unique(d))
        d = []
    return(j)
      

# a different approcah using sets and list comprehension
def ans_counts_task(data_merged):
    print(data_merged)
    return ((sum([len(set(data_merged))])))

def ans_count_task2(data):
    total = 0
    for item in data :
        k = map(set,item)
        common = set.intersection(*map(set,item))
        total +=len(common)
    print(total)


def test(data):
    print('data',data)
    for string in data:
        print('string',string)
        for letter in string:
            print('letter',letter)
            for char in letter:
                print('char',char)
    



data,data_merged = parse_data(filename)
result = ans_counts(data)
print('The sum of answers is :',result)
# ans_counts_task(data_merged)
ans_count_task2(data)

