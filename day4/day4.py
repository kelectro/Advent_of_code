import numpy as np
filename = '/home/kiagkons/Desktop/advent of code/day4/passports.txt'


def is_valid_task1(passports):
    # print(passports)
    p=0
    valid_fields = ['byr' ,'iyr' ,'eyr' ,'hgt' ,'hcl' ,'ecl' ,'pid']
    for k in passports.keys():
        if k in valid_fields:
            p+=1
    if p == 7 :
        return 1
    else:
        return 0


def is_valid_task2(passport):
    eye_color = ['amb','blu','brn','gry','grn','hzl','oth']
    valid_height = False  
    valid_col = False
   
    valid_birth = 1920 <= int(passport.get('byr', False)) <= 2002 and len(str(passport.get('byr',False))) == 4

    valid_issue = 2010 <= int(passport.get('iyr',False)) <= 2020 and len(str(passport.get('iyr',False))) == 4

    valid_expiration = 2020 <= int(passport.get('eyr', False)) <=2030 and len(str(passport.get('eyr', False))) == 4

    hgt = passport.get('hgt', False)

    if hgt != False and hgt[-2:] == "cm":
        valid_height = 150 <= int(hgt[:-2]) <= 193
    elif hgt != False and hgt[-2:] == 'in':
        valid_height = 59 <= int(hgt[:-2]) <= 76

    col = str(passport.get('hcl',False))
    if col!= False and col[0] == '#':
        valid_col = len(str(col[1:])) == 6 and col[1:].isalnum() 
    valid_ecol = passport.get('ecl',False) in eye_color
    valid_pid = len(str(passport.get('pid',False))) == 9
    
    return(valid_birth and valid_issue and valid_expiration and valid_height and valid_col and valid_ecol and valid_pid)
    
   

def parse_input(path):
    with open(path,'r') as file:
        data = file.read()
    
    data = data.split('\n\n')
    data = [data.replace('\n', ' ') for data in data]
    data = [data.split() for data in data]
    return data
    
def create_dict(data):
    passports = {}
    for line in data:
        pair = line.split(":")
        key = pair[0]
        value = pair[1]
        passports[key]=value

    return(passports)
    


      




data = parse_input(filename)
passports = [create_dict(item) for item in data]
valid_pass = [is_valid_task1(person) for person in passports]
print('Total number of valid passports is :',np.sum(valid_pass))
task2_valid = [is_valid_task2(person) for person in passports]
print('Total number of valid passports for task 2 are : ',task2_valid.count(True))