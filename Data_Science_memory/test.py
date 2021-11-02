import pandas as pd
from pandas.core.tools.datetimes import to_datetime
import re 

def get_year_release(arg):
    #находим все слова по шаблону "(DDDD)"
    candidates = re.findall(r'\(\d{4}\)', arg) 
    # проверяем число вхождений
    if len(candidates) > 0:
        #если число вхождений больше 0,
	#очищаем строку от знаков "(" и ")"
        year = candidates[0].replace('(', '')
        year = year.replace(')', '')
        return int(year)
    else:
        #если год не указан, возвращаем None
        return None


rating_movies_data = pd.read_csv('C:/Python/ratings_movies/ratings_movies.csv', sep=',')

ratings_df = rating_movies_data.copy()
#print(ratings_df)

#12.8.1
ratings_df['year_release'] = ratings_df['title'].apply(get_year_release)
#print(ratings_df.info())

#12.8.2
for_1999 = ratings_df[(ratings_df['year_release'] == 1999)]
ratings_1999 = for_1999.groupby(['title'])['rating'].mean()
#print(ratings_1999.sort_values())

#12.8.3
for_2010 = ratings_df[(ratings_df['year_release'] == 2010)]
ratings_2010 = for_2010.groupby(['genres'])['rating'].mean()
#print(ratings_2010.sort_values())

#12.8.4
user_fan = ratings_df.groupby('userId')['genres'].nunique().sort_values()
#print(user_fan)
