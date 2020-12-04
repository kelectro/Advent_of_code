import re

filepath = '/home/kiagkons/Desktop/advent of code/day2/passwords.txt'

class Password:
    def __init__(self,path,case) :  
        self.valid_count = 0
        self.case = case
          
        # self.test = ['1-3 a: abcde']        
        self.path = path
        self.load_data()

        if self.case == 1 :
            self.check_pass()
        elif self.case == 2 :
            self.check_pass_rule2()
        
    def load_data(self):

        self.element = []

        self.file = open(self.path,'r')
        for self.line in self.file:
            self.element.append(re.split('-| |: |\n',self.line))
        self.file.close()

    def check_pass(self):
        for i in range(len(self.element)):
            self.occ  = self.element[i][3].count(self.element[i][2])
            if self.occ >= int(self.element[i][0]) and self.occ <= int(self.element[i][1])  :
                self.valid_count = self.valid_count +1
        print('The number of valid passwords is : \n ', self.valid_count)

    def check_pass_rule2(self):
        for i in range(len(self.element)):
            self.lower = int(self.element[i][0])
            self.upper = int(self.element[i][1])
            if self.element[i][2] == self.element[i][3][self.lower-1] and self.element[i][2] != self.element[i][3][self.upper-1]:
                self.valid_count +=1
            elif self.element[i][2] != self.element[i][3][self.lower-1] and self.element[i][2] == self.element[i][3][self.upper-1]:
                self.valid_count +=1
        print('The number of valid passwords is : \n ', self.valid_count)
                

pwd=Password(filepath,case=1)
