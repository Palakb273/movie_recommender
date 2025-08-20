import pandas as pd
from mysqlboilerplate import run_query
from preprocess import parse_genres, parse_actors, parse_director
movies=pd.read_csv("C:/Users/palak/OneDrive/Desktop/movie_analysis/tmdb_5000_movies.csv")
credit=pd.read_csv("C:/Users/palak/OneDrive/Desktop/movie_analysis/tmdb_5000_credits.csv")
movies=movies.merge(credit,left_on="id",right_on="movie_id")
print("dataset loaded")
movies.drop_duplicates(subset="id",inplace=True)
print(movies.isnull().sum())
movies["overview"]=movies["overview"].fillna("")
movies["genres_clean"]=movies["genres"].apply(parse_genres)
movies["actors_clean"]=movies["cast"].apply(parse_actors)
movies["director_clean"]=movies["crew"].apply(parse_director)
movies_table=movies[["id","title_x","vote_average","overview","release_date","genres_clean","actors_clean","director_clean","vote_count"]].copy()
movies_table["release_year"]=pd.to_datetime(movies_table["release_date"],errors="coerce").dt.year
movies_table.to_csv("C:/Users/palak/OneDrive/Desktop/movie_analysis/clean_movies.csv",index=False)
print("cleaning completed")
