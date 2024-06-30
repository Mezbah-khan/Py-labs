#  Hello world this is mezbah khan form backend developer 
#  lets create a project with pandas laibary examples and  action performs 
#  Lets  do  this  with proper codes 
    
import numpy as np 
import pandas as pd

    # lets create the dataset 
dataset01 = { 
      'name'  : ['mezbah','istiak', 'noman','mamun',np.nan, 'sagor','sakil','Tomo'], 
      'age'   : [17,25,26,np.nan, 23,np.nan, 28,30],
    'salaries': [100,0,np.nan, 12000,25000,np.nan,np.nan,20000],
   'locations': [np.nan,'patuakhali',np.nan,'borishal','dhaka','kumillah','chitagong',np.nan] } 

    # frist lets check this datas lenth and attributes 
print(len(dataset01['name']))      # output --> 8 
print(len(dataset01['age']))       # output --> 8 
print(len(dataset01['salaries']))  # output --> 8 
print(len(dataset01['locations'])) # output --> 8 

    # lets create some numericcal value for this example
    
var1 = [1,3,6,11,13,18,23,25,32,36,47,51]
var2 = [53,57,62,63,68,72,79,81,86,92,95,99]
   
   # lets create the dataframe to move forword 
   
dataframe= pd. DataFrame(dataset01)
print(dataframe)

            # this is output  #
  #    name   age  salaries   locations
  # 0  mezbah  17.0     100.0         NaN
  # 1  istiak  25.0       0.0  patuakhali
  # 2   noman  26.0       NaN         NaN
  # 3   mamun   NaN   12000.0    borishal
  # 4     NaN  23.0   25000.0       dhaka
  # 5   sagor   NaN       NaN    kumillah
  # 6   sakil  28.0       NaN   chitagong
  # 7    Tomo  30.0   20000.0         NaN

   # lets create the dataframe to csv file 
csv_file  = dataframe.to_csv('datafile01.csv')
print(csv_file)

   # lets create the excele with this dataframe 
excel_file = dataframe.to_excel('datafile01.xlsx')
print(excel_file)
    
   # lets take action in this dataset 
   # first lets chcekout the series of this data 
   
pd_series0_01= pd. Series(var1)
print(pd_series0_01)

pd_series_02 = pd. Series(var2)
print(pd_series_02)

    # lets checkout the datatypes ofd thi s datas 
print(dataframe.dtypes)
print(pd_series0_01.dtype)
   
   # Now lets start with our main codes 
   # frist lets ceckout the datas with head() 
   
data_check_01 = dataframe.head(5)
print(data_check_01)

print('\n\n')

    # last 5 datas with tails () 
data_check_02 = dataframe. tail(5)
print(data_check_02)


    # let know the baic info about this data
data_check_03  = dataframe. info()
print(data_check_03)

    # okh we get information in this dataset 
    # lets upadte with discribtions like discrib() method 
    
data_check_04 = dataframe.describe()
print(data_check_04)

data_check_05 = dataframe.describe().sum()
print(data_check_05)

    # we got out standing data describtions in this note 
    # lets findout the null  values an perfurm actions 

data_check_06 = dataframe.isnull()
print(data_check_06)

data_check_07 = dataframe.isnull().sum()
print(data_check_07)

    # we found so many nulll values in this dataframe 
    #  lets modify with methods and handle the missing values 
    
data_check_08 = dataframe.duplicated()
print(data_check_08)    #output --> There is no duploicate daat 

data_check_09 = dataframe.duplicated().sum()
print(data_check_09)    # output --> 0 
