import pandas as pd
movies = pd.read_csv('data/movies.csv')
ratings = pd.read_csv('data/ratings.csv')
tags = pd.read_csv('data/tags.csv')

print(movies.shape, ratings.shape, tags.shape)
print(movies.head())
ratings['rating'].describe()
