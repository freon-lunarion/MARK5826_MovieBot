import pandas as pd 
import ast

# read dataset
# movies_metadata_sample is faster to preprocess 
# movies_metadata has bigger record but slower to preprocess
metadata = pd.read_csv('data/movies_metadata_sample.csv', low_memory=False)
# metadata = pd.read_csv('data/movies_metadata.csv', low_memory=False)

# we drop some rows because doesn't have data (N/A) on some columns 
metadata = metadata.dropna(subset=['imdb_id','poster_path'])
# we drop some columns because unimportant for our process
metadata = metadata.drop(['belongs_to_collection','homepage','popularity','tagline','status'],axis=1)
metadata = metadata.drop(['runtime','release_date','original_language','production_countries','production_companies','spoken_languages','video'],axis=1)

# reformat data on certain columns
metadata['genres'] = metadata['genres'].apply(lambda x: ast.literal_eval(x))
metadata['genres'] = metadata['genres'].apply(lambda x: ', '.join([d['name'] for d in x]))
metadata['imdbURL'] = 'https://www.imdb.com/title/' + metadata['imdb_id'] + '/'
metadata['tmdbURL'] = 'https://www.themoviedb.org/movie/' + metadata['id']
metadata['ImageURL'] = 'https://image.tmdb.org/t/p/w92' + metadata['poster_path']


# write prepared data to new csv file
metadata.to_csv('data/metadata_prep.csv')

