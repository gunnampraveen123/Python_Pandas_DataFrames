# importing pandas package
import pandas as pd

# read csv file  as dataframe
titanic_df=pd.read_csv('titanic.csv')
pd.set_option('display.max_rows', None)
print(titanic_df)

# want to extract records whose sex is male
titanic_df=titanic_df[titanic_df['Sex'] == 'male']
print(titanic_df)

# want to extract records Sex not female
titanic_df=titanic_df[titanic_df['Sex'] != 'female']
print(titanic_df)

# Derive New_Age column from existing DataFrame column Age
titanic_df['New_Age']=titanic_df['Age']+5
print(titanic_df)

# Want to extract records whose age greater than 25 and less than 30
titanic_df=titanic_df[ (titanic_df['Age'] > 25) & (titanic_df['Age'] < 30)]
print(titanic_df)

# Want to extract records whose age greater than or equal to 30
titanic_df=titanic_df[ (titanic_df['Age'] > 30) | (titanic_df['Age'] == 30)]
print(titanic_df)
  