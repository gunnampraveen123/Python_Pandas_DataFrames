# import pandas pacakage , give it alias name
import pandas as pd

# create a Dataframe from Dictionary 
Dict={'cars':['dzire','innova','i20','etios','Ertiga'],
    'price':['8,00,000','25,00,000','7,00,000','12,00,000','14,00,000']}
DF=pd.DataFrame(Dict)
print(DF)

# Read first Two records in Dataframe
DF1=DF.head(2)
print(DF1)

# Read last Two records in Dataframe
DF1=DF.tail(2)
print(DF1)

# Read only particular column 
DF1=DF['cars']
print(DF1)

# add a new column to existing Dataframe
DF['Colour']=['red','black','white','blue','gray']
DF1=DF
print(DF1)

# add column to existing dataframe 
DF['seating']=['4','7'] # Error ValueError no.of records not matching
DF1=DF # ValueError: Length of values (2) does not match length of index (5)
print(DF1)

# create a DataFrame from a csv file 
titanic_df=pd.read_csv('titanic.csv')

# read a dataframe,if a dataframe consists of large no.of records it only display first,last five records
print(titanic_df)

# read a dataframe only first five records
titanic1=titanic_df.head() # head read only 5 records defaultly
print(titanic1)

# read a dataframe only last five records
titanic1=titanic_df.tail() # defaultly read only 5 records
print(titanic1)

# read first 10 records in a dataframe
titanic1=titanic_df.head(10) 
print(titanic1)

# read last 10 records in a dataframe 
titanic1=titanic_df.tail(10)
print(titanic1)

# Read records based on position by using loc. iloc
# read only 6th record in dataframe
titanic1=titanic_df.loc[5]
print(titanic1)

# read 5,6,7,8,9 records in a dataframe
titanic1=titanic_df.loc[5:9]
print(titanic1)

# read all records in a dataframe 
titanic1=titanic_df.loc[:]
print(titanic1)

# read even records records
titanic1=titanic_df.loc[::2] 
print(titanic1)

# read odd records in a dataframe
titanic1=titanic_df.loc[1::2]
print(titanic1)

# Read records by using step value, it will read 3 , 6, 9, .. 
titanic1=titanic_df.loc[::3]
print(titanic1)

# read particular records with a single column
titanic1=titanic_df.loc[5:10,'Age']
print(titanic1)

# read particular records with a multiple columns
titanic1=titanic_df.loc[4:8,['Name','Age','Sex']]
print(titanic1)

# read particular columns with all records
titanic1=titanic_df.loc[:,['Name','Age','Sex']]
print(titanic1)

# read records and columns based on index wise
# we can use iloc for indexing , starts with 0 for coulmn and rows 
titanic1=titanic_df.iloc[5:10, 2:5] # we read 5,6,7,8,9 records with  3,4,5 columns
print(titanic1)

# read  3,5,7 columns with all records
titanic1=titanic_df.iloc[:,3:8:2]
print(titanic1)

# read all columns with all records 
titanic1=titanic_df.iloc[:,:]
print(titanic1)

# add new column to existing dataframe
titanic_df['S.No']=range(1,892)
titanic1=titanic_df.head()
print(titanic1)

