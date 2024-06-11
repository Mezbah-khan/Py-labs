# helloworld this is mezbah khan from  backend dveeloepr 
# l ets creat  an AI model 
#  lets d o this 

import numpy as np

# Let's create a class
class Mezbah:
    def __init__(self, loop):
        self.loop = loop 
        
    # Let's create a static method to welcome the user
    @staticmethod
    def hello():
        print('Hello user, this is your loop:')
        
    def val_loop(self, start, end):
        self.loop = 0
        str_dta = np.arange(start + 1, end + 1)  # Create an array with the loop data
        for val in str_dta:
            print(val)
        return str_dta
        
frist_idx = int(input('Enter your starting index: '))
secend_idx = int(input('Enter your stopping index: '))

# Let's create an object for our class
system_check = Mezbah(0)
system_check.hello()
dis_loop_dta = system_check.val_loop(frist_idx, secend_idx)
print('This is loop data in array format:', dis_loop_dta)

   # This is another project (2th ) --> 




