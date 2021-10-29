import pandas as pd
from pandas.core.tools.datetimes import to_datetime

melb_data = pd.read_csv('C:\Python\melb_data_fe.csv', sep=',')
melb_df = melb_data.copy()
#print(melb_df.head())
print(melb_df.info())

date1 = pd.to_datetime('2017-05-01')
date2 = pd.to_datetime('2017-09-01')
melb_df['Date'] = to_datetime(melb_df['Date'])
mask1 = (date1 <= melb_df['Date']) & (melb_df['Date'] <= date2)
print(
    melb_df[mask1].groupby(by='SellerG')['Price'].sum().sort_values()
    )

