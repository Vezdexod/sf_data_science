import pandas as pd

def time_of_day(times):
    if 0<=times<=6:
        return 'night'
    elif 6<times<=12:
        return 'morning'
    elif 12<times<=18:
        return 'day'
    else:
        return 'evening' 

citybike_data = pd.read_csv('C:\Python\citibike-tripdata.csv', sep=',')

citybike_df = citybike_data.copy()

#print(citybike_df.head())
#print(citybike_df.info())

citybike_df['starttime'] = pd.to_datetime(citybike_df['starttime'])

time_day = citybike_df['starttime'].dt.hour
citybike_df['time_of_day'] = time_day.apply(time_of_day)
print(citybike_df['time_of_day'].value_counts())
