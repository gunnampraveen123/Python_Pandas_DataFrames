# importing pandas package
import pandas as pd

# read csv file in dataframe
st_df = pd.read_csv('Stocks.csv')

# view info of the dataframe
print(st_df.info())

# convert date column object data type to datetime data type
st_df['date'] = pd.to_datetime(st_df['date'])

# extract year from date column
print(st_df['date'].dt.year)

# convert high float64 to float32
st_df['high']=st_df['high'].astype('float32')
print(st_df.info())

# convert volume int64 to float64 
st_df['volume']=st_df['volume'].astype(float)
print(st_df.info())

# convert date column  object to datetime 
st_df['date']=st_df['date'].astype('datetime64[as]')
print(st_df.info())
print(st_df)