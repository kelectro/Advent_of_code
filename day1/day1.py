import itertools
# from itertools import combinations

filepath = '/home/kiagkons/Desktop/advent of code/day1/input.txt'

class Cmb:
    def __inint__(self,path):
        pass
        
    def read_file(self,path, param):
        self.param = param
        self.path = path
        self.input_data = open(self.path, 'r', newline='\n')
        self.data = [int(x.strip()) for x in self.input_data.readlines()]
        self.input_data.close()

        self.data = list(self.data)
        return(self.compare())

    def compare(self):
        self.combs = itertools.combinations(self.data, self.param)
        for component in self.combs :
            # print(component[0],component[1])
            if component[0] + component[1] + component[2] == 2020 :
                self.result = component[0]*component[1]*component[2]
                # print(self.result)
        return(self.result)


comp = Cmb()
result = comp.read_file(filepath,3)
print(result)
