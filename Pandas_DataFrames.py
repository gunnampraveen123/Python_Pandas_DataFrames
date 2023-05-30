# importing pandas package
import pandas as pd

# read a csv file as dataframe 
titanic_df=pd.read_csv('titanic.csv')
print(titanic_df)

# datatype of each series on dataframe , here series means column
titanic_df=titanic_df.dtypes # display column with data type
print(titanic_df)

# display each column count, mean, std, min, max , etc values based on datatype 
titanic_df=titanic_df.describe()
print(titanic_df)

# display count, mean, max, min etc values on particular column
titanic_df=titanic_df['Age'].describe()
print(titanic_df)

# display metadata of a DataFrame
titanic_df=titanic_df.info()
print(titanic_df)

# display only object datatype columns
df_dtype=titanic_df.dtypes[titanic_df.dtypes == 'object'].index
print(df_dtype)

# display metadata of particular datatype of columns
df_dtype=titanic_df.dtypes[titanic_df.dtypes == 'object'].index
titanic_df=titanic_df[df_dtype].describe()
print(titanic_df)