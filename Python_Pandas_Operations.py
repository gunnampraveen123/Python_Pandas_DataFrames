# pandas is a python library , which is used analyze the data from large datasets
# install the pandas package , $ pip install pandas
# It is used to analyzing , cleaning , exploring , manipulating data
# First we have import pandas , whenever we write a programme

import pandas
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pandas.DataFrame(mydataset)
print(myvar)
import pandas as pd
print(pd.__version__) # version of pandas 


# What is pandas Series 
# It is a one dimesional array / table with  columns
# pandas series 

import pandas as pd
a=[1,2,3,6,10,7,3,5,8,4]
s=pd.Series(a)
print(s)
print(s[0]) 
print(s[4])
print(s[1:5])
print(s[1:5:2]) # dtype: int64

# labels

import pandas as pd
a=[1,3,5]
l = pd.Series(a,index=['x','y','z'])
print(l)
print(l['x'])

# key value object as a series

import pandas as pd
calories= {'day1':822,'day2':292, 'day3':299}
d = pd.Series(calories)
print(d)
d1 = pd.Series(calories, index = ["day1", "day2"])
print(d1)

# create a dataframe from two series

import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df= pd.DataFrame(data)
print(df)


# Pandas DataFrame are 2 dimensional data structure / table with rows and columns

import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df) 
#refer to the row index:
print(df.loc[0])
print(df.loc[1])
# use a list of indexes:
print(df.loc[[0, 1]])

# named indexes 
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)
# refer to the named index:
print(df.loc["day2"])

# load files into a dataframe
import pandas as pd
df=pd.read_csv('ex.csv')
print(df)


# pandas Read CSV files

import pandas as pd
df = pd.read_csv('data.csv')
print(df.to_string()) 


# pandas read_csv is read first 5 rows and last 5 rows
import pandas as pd
df = pd.read_csv('data.csv')
print(df) 

import pandas as pd
print(pd.options.display.max_rows)  # 60 

import pandas as pd
pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df) 

# Load the JSON file into a DataFrame

import pandas as pd
df = pd.read_json('data1.json')
print(df.to_string())

import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}
df = pd.DataFrame(data)
print(df) 

import pandas as pd
df = pd.read_csv('data.csv')
print(df.head(10))


import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())

import pandas as pd
df = pd.read_csv('data.csv')
print(df.tail())

import pandas as pd
df = pd.read_csv('data.csv')
print(df.tail(10))

import pandas as pd
df = pd.read_csv('data.csv')
print(df.info())

# Data Cleaning
# Data Cleaning means fixing bada data in a data set
# Bad data means
# Empty cells
# Data in wrong format
# wrong data
# Duplicates

# empty cells 
# remove rows
# Return a new data set with no empty cells

import pandas as pd
df=pd.read_csv('data.csv')
new_df=df.dropna() #by defualt dropna method returns a new dataframe , will not change the original
print(new_df.to_string())


import pandas as pd
df=pd.read_csv('data.csv')
df.dropna(inplace=True) # will not return new dataframe, but it will remove rows containing null values
print(df.to_string())

# Replace Empty values
import pandas as pd
df=pd.read_csv('data.csv')
df.fillna(130,inplace=True)
print(df.to_string())

# Replace only specified column 

import pandas as pd
df=pd.read_csv('data.csv')
df['Calories'].fillna(110,inplace=True)
print(df.to_string())

# Replace Using mean, mode , median

import pandas as pd
df=pd.read_csv('data.csv')
new_df=df['Calories'].mean()
df['Calories'].fillna(round(new_df),inplace=True)
print(df.to_string())

import pandas as pd
df=pd.read_csv('data.csv')
new_df=df['Calories'].mean()
df['Calories'].fillna(new_df,inplace=True)
print(df.to_string())

import pandas as pd
df=pd.read_csv('data.csv')
new_df=df['Calories'].median()
df['Calories'].fillna(new_df,inplace=True)
print(df.to_string())

import pandas as pd
df=pd.read_csv('data.csv')
new_df=df['Calories'].mode()[0]
df['Calories'].fillna(new_df,inplace=True)
print(df.to_string())

# Cleaning data of wrong format

import pandas as pd
df=pd.read_csv('data1.csv')
df['Date']=pd.to_datetime(df['Date'])
print(df.to_string())
# remove the row 
df.dropna(subset=['Date'],inplace=True)

# Pandas Fixing Wrong Data 
# wrong data is identified in dataset how the data is look like
# to fix the data we replace
# in sample data set we have duration in row 7 is 450 we change to 45 based on dataset
import pandas as pd
df=pd.read_csv('data.csv')
df.loc[7,'Duration'] =45

print(df.to_string())

import pandas as pd
df=pd.read_csv('data.csv')
df.loc[69,'Duration'] =45
print(df.to_string())

# when it comes to large datasets we can set boundaries
import pandas as pd
df=pd.read_csv('data.csv')
for x in df.index:
    if df.loc[x,'Duration']>120:
        df.loc[x,'Duration']=120
print(df.to_string())

# Removing duplicates

# discovering duplicates
import pandas as pd
df=pd.read_csv('data.csv')
print(df.duplicated().to_string())


# removing duplicates
import pandas as pd
df=pd.read_csv('data.csv')
df.drop_duplicates(inplace=True)
print(df.to_string())


# Pandas - Data Correlations
import pandas as pd
df=pd.read_csv('data.csv')
print(df.corr())

# correlation means the relation b/t columns 
# 1 to 1 is a perfect correlation
# the corerelation b/t 1 to -1

# perfect correlation is 1
# good correlation is 0.9 to 0.6 /-0.6
# Bad correlation is below 0.6

# Pandas Plotting

import pandas as pd
import matplotlib.pyplot as plt  # we install matplotlib package # pip install matplotlib
df=pd.read_csv('data.csv')
df.plot()
plt.show()
print(df.to_string())

# Scatter plot

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('data.csv')
df.plot(kind='scatter', x='Duration', y='Calories')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('data.csv')
df.plot(kind='scatter', x='Duration', y='Maxpulse')
plt.show()

# Hisotogram

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('data.csv')
df['Duration'].plot(kind='hist')
plt.show()

# filter the records 
import pandas as pd 
df=pd.read_csv('titanic.csv')
print(df[df['Age']>35])
