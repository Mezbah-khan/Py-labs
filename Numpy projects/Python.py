# hello wrold this is mezbah khan form backend developer.lets create an array  with numpy and linked with fucntion of [python] dataset 
# Also add an loop function for data for input user like(Customer or datausers). So lets do this woth proper codes in python language 

import numpy as np
class Mezbah:
    def __init__(self, file_int):
        self.file_int = file_int
        self.file_fnt = [int(i) for i in file_int.split(',')]
        self.svt_dta = np.array(self.file_fnt)
        
    def hello():
        print('Hello wrold')
        
    def input_dta(self):
        return self.file_fnt

    def save_dta(self):
        return self.svt_dta

file_int = input("Enter your data: ")
system_check = Mezbah(file_int)
print('This is your data as array : ', system_check.save_dta()) 




