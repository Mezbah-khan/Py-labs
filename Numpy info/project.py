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

# Hello wrold this is mezbah khan form backend developer
# Lets build a project on python usiing the  numpy laibary 
# Lets do this with proper codes 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
class project:
    hello = 'Hello everyone in this project --> '

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    @staticmethod
    def warning():
        return 'Only personal data for this code'

    def function_val(self):
        with open("demo.txt", 'w+') as file:
            if isinstance(self.name, str):
                file.write(self.name + '\n')
            else:
                print('Enter valid data for name')

            if isinstance(self.age, int):
                file.write(str(self.age) + '\n')
            else:
                print('Enter valid data for age')

            if isinstance(self.email, str):
                file.write(self.email + '\n')
            else:
                print('Enter valid data for email')

user_input_name = input('Enter your name: ')
user_input_age = int(input('Enter your age: '))
user_input_email = input('Enter your email: ')

# Create an instance of the project class
system_check = project(user_input_name, user_input_age, user_input_email)

# Call methods without parentheses
print(system_check.hello)
print(system_check.warning())
system_check.function_val()


    # we have succesfully created a new project with proper codes
    # Lets move on ouur 3rd project (3rd) -->




