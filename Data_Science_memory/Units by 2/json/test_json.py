import pandas as pd

df = pd.read_csv('C:/Python/github/sf_data_science/Data_Science_memory/Units by 2/json/recipes.csv')
print(df.head())

ingredients = list(df.columns)[3:] # Создаем список уникальных значений ингредиентов
print(ingredients)

