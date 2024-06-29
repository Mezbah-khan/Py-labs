# helloo wrold this is mezbah khan from backend developer 
# Lets create an info  with examples of numpy laibaries 
# Lets build this project with proper codes 

import numpy as np 

arr1  = [1,2,3,4,5,6,7]
arr2 = [8,9,10,11,12,13,14]
  
    # Lets create a 2D dimentional array 
arr3 = ([[10,20,30,40],[50,60,70,80]])
arr4 = ([[5,6,7,9],[10,11,12,13]])

    # Lets stat the operations with (EX +[1,2,3,......+ n ])
    # Lets create an array with identifiers 

ex01 = np.array (arr1)
ex02 = np.array(arr3)
   
    # Lets print both of them
print(ex01,ex02)

    # Lets create a new array without identifiers 

ex03 = np .array ([100,200,300,400,500])
ex04 = np.array ([[100,200,300,400,500],[600,700,800,900,1000]])

    # Lets print both of them
print(ex03,ex04)

    # BOTH arrays example is succesfullly created 
    # Lets use the zero method of numpy
    
ex05 = np.zeros((3,5))
print(ex05)   #output --> [ 3 is times row and 5 is values ]

    # Lets use the full method and pass the valiue with 10times rows 
    
ex06 = np.full((10,3),4)
print(ex06)  #Output --> [10 is times of row,4 is value  and 3 is length ]

    # lets use the arange function in numpy 
    
ex07 = np.arange(10,18)
print(ex07)  #Output --> [10 11 12 13 14 15 16 17]

     # Using the step option in  arage 

ex08 = np.arange(10,100,5)
print(ex08)  #output --> [10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95]

     # Using basic mathmetic in this operation 

ex09 = np.arange(11-1 , 100 +1 )
print(ex09)  # Output --> [started with 10 and end on 100 exactly ]

     # Lets use the rand and randint method of numpy with example 
     
ex10 = np.random.rand(1,2)
print(ex10)  # Output --> [0.964835 0.943272]

     # Lets use the randint method of numpy with example
     
ex11 = np.random.randint(0,7)
print(ex11)  # output --> [3,4,4,5,2,1,0] 

    # Lets given array and ordered to selcet any specific number 
import numpy as np

ex12 = np.random.rand(10, 10)
print(ex12)
    
    # The is succesfully printed 
    # Lets find the shapes of arrs and reshape it 
    
ex13 = np.shape(arr1)
print(ex13)  # Output --> (7,) CAUSE there are 7 values in the array

ex14 = np.shape(arr3)
print(ex14)  # Output --> (2, 4) CAUSE there are 2 rows and 4 values in each row

    # Lets find the shapes of arrs and reshape it
ex15 = np.reshape(ex04, (2, 5))
print(ex15)

   # Lets create array use all joining method of numpy
   
ex16 = np.add(arr1,arr2)
print(ex16)  # Output --> [9,11,13,15,17,19,21]

ex17 = np.subtract(arr3,arr4)
print(ex17)  # Output --> [[0,0,0,0],[0,0,0,0]]


    # Lets concatinate the data as array 
ex18 = (arr1 + arr2)
ex19 = (arr3 + arr4)

print(ex18,ex19)
    

      # Lets use the comncatinate method 
      
ex20 = np.concatenate((arr1,arr2),axis=0)
print(ex20)   # Output --> [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

    # Lets add those array horizontally 
      
ex21 = np.hstack((arr1,arr2))
print(ex21)
 
ex22 = np.vstack((arr3,arr4))
print(ex22)

      # Lets create two new array as insert some common data in the array 
      
new_array01 = np. array ([12,13,14,15,16,17,18,19,20])
print(new_array01) 

    # Lets add those array horizontally 
      
ex21 = np.hstack((arr1,arr2))
print(ex21)
 
ex22 = np.vstack((arr3,arr4))
print(ex22)

      # Lets create two new array as insert some common data in the array 
      
new_array01 = np. array ([12,13,14,15,16,17,18,19,20])
new_array02 = np.array ([15,16,17,18,19,20,21,22,23])

check_data01  = np.intersect1d(new_array01, new_array02)
print(check_data01)   #output common data ---> [15 16 17 18 19 20]

     # Lets remove un-common data 
    
check_data02 = np.setdiff1d (new_array01,new_array02)
print(check_data02)  #output --> [12 13 14]

     # Lets slice the codes with numpy methods
     
ex23 = arr1.copy()
slice01 =(ex23[0:])
print(slice01) #output --> [1, 2, 3, 4, 5, 6, 7] = 6 index 

slice02 = (ex23[:6])
print(slice02)  #output ---> [1, 2, 3, 4, 5, 6]

slice03 = (ex23[2:5])
print(slice03)  #output --> [3, 4, 5]

slice04 = (ex23[:2]) 
print(slice04) #output ---> [1, 2]

    # Lets add the values with functions
ex24= np.add(arr1,arr2)
print(ex24)   #output--> [ 9 11 13 15 17 19 21]

ex25 = np.subtract(arr3,arr4)
print(ex25) #output --> [[ 5 14 23 31] , [40 49 58 67]]

ex26 = np.multiply(arr1,arr2)
print(ex26) #output --> [ 8 18 30 44 60 78 98]

ex27 = np.divide(arr3,arr4)
print(ex27)  #output --> [[2.         3.33333333 4.28571429 4.44444444] [5.         5.45454545 5.83333333 6.15384615]]

     # lets perform action in this example 

ex28 = np.sum(arr1) 
print(ex28) # output --> 28 

ex29 = np.max(arr4)
print(ex29) #output --> 13

ex30 = np. min(arr3)
print(ex30) #output --> 10 

ex31 = np.mean(arr4)
print(ex31)  #output --> 9.125

ex32 = np.cumsum(arr2)
print(ex32)  #output --> [ 8 17 27 38 50 63 77]

ex33 = np.cumprod(arr1) 
print(ex33)  #output -->  [  1    2    6   24  120  720 5040]

   
    # lets try something else 
ex34 = np.transpose(arr3)
print(ex34)   #output--> [[10 50] [20 60][30 70] [40 80]] 

    # lets create an multiple array 
    
a = np.array([[[1, 2, 3], 
               [4, 5, 6]], 
              
              [[7, 8, 9], 
               [10, 11, 12]]])

b = a .flatten()
print('original value : ',a, '\nflatten value : ',b)
    # next time more must be 
    

     
