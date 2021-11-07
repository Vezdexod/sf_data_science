import pandas as pd
from pandas.core.tools.datetimes import to_datetime
import re 

covid_data = pd.read_csv('C:/Python/PYTHON-13/covid_data.csv', sep=',')
vac_data = pd.read_csv('C:/Python/PYTHON-13/country_vaccinations.csv', sep=',')
covid_df = covid_data.copy()
vac_df = vac_data.copy()
vac_df = vac_df[
    ['country', 'date', 'total_vaccinations', 
     'people_vaccinated', 'people_vaccinated_per_hundred',
     'people_fully_vaccinated', 'people_fully_vaccinated_per_hundred',
     'daily_vaccinations', 'vaccines']
]
print(covid_df.head())
print(vac_df.head())









