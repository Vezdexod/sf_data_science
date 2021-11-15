import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px



hhru_data = pd.read_csv('C:/Python/github/sf_data_science/PROJECT-1/dst-3.0_16_1_hh_database.csv', sep=';')

hhru_df = hhru_data.copy() # уДАЛИТЬ

def rename_currency(currrency):
    if currrency == 'руб.':
        return 'RUB'
    elif currrency == 'бел.руб.':
        return 'BYN'
    elif currrency == 'грн.':
        return 'UAH'
    elif currrency == 'сум':
        return 'UZS'
    else:
        return currrency
    

currancy_data = pd.read_csv('C:/Python/github/sf_data_science/PROJECT-1/ExchangeRates.csv', sep=',')
currency_df = pd.DataFrame()
currency_df['currency'] = currancy_data['currency']
currency_df['date'] = pd.to_datetime(currancy_data['date']).dt.date
currency_df['proportion'] = currancy_data['proportion']
currency_df['close'] = currancy_data['close']
currency_df['Курс'] = currency_df['close']/currency_df['proportion']

hhru_df['Дата создания резюме'] = pd.to_datetime(hhru_df['Обновление резюме']).dt.date
hhru_df['сумма ЗП'] = hhru_df['ЗП'].apply(lambda x: (x.split()[0]))
hhru_df['сумма ЗП'] = hhru_df['сумма ЗП'].astype('float64')
hhru_df['валюта ЗП'] = hhru_df['ЗП'].apply(lambda x: (x.split()[1]))
hhru_df['валюта ЗП'] = hhru_df['валюта ЗП'].apply(rename_currency)

#Соединим hhru_df и currency_df
hhru_df = hhru_df.merge(
    currency_df,
    left_on=['валюта ЗП','Дата создания резюме'],
    right_on=['currency','date'],
    how='left'
)

#Добавим признак зарплаты в рублях
#mask_RUB = (hhru_df['валюта ЗП'] == 'RUB')
#mask_no_RUB = (hhru_df['валюта ЗП'] != 'RUB')
#hhru_df[mask_RUB]['Курс'] = np.float64(1)
'''hhru_df['Курс'] = hhru_df['Курс'].apply(lambda x: 1 if x is np.NaN else (x))
hhru_df['ЗП руб.'] = hhru_df['сумма ЗП']*hhru_df['Курс']


#display(hhru_df[mask_RUB].head(3))
#display(hhru_df[mask_no_RUB].head(3))
display(hhru_df.iloc[80:82])
#display(hhru_df.info())
display(hhru_df.median())'''

def renan(cours):
    if cours == nan:
        return 1
    else:
        return cours


hhru_df['Курс2'] = hhru_df['Курс'].apply(renan) 
print(hhru_df['Курс2'])
#hhru_df['Курс'] = hhru_df['Курс'].apply(lambda x: 1 if x is np.NaN else (x))
hhru_df['ЗП руб.'] = hhru_df['сумма ЗП']*hhru_df['Курс']
print(hhru_df.iloc[80:82])