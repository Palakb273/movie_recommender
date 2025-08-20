import pandas as pd
movies=pd.read_csv("C:/Users/palak/OneDrive/Desktop/movie_analysis/clean_movies.csv")
movies["genres_clean"]=movies["genres_clean"].apply(lambda x: eval(x) if isinstance(x, str) and x.startswith("[") else [])
movies["actors_clean"]=movies["actors_clean"].apply(lambda x: eval(x) if isinstance(x, str) and x.startswith("[") else [])
movies["director_clean"] = movies["director_clean"].apply(lambda x: str(x).strip()if pd.notna(x)else"")
all_genres=set(g for i in movies["genres_clean"]for g in i)
for g in all_genres:
    movies[g]=movies["genres_clean"].apply(lambda x: 1 if g in x else 0)
all_actors=pd.Series([a for i in movies["actors_clean"]for a in i])
top_actors=all_actors.value_counts().head(20).index
for actor in top_actors:
    movies[actor]=movies["actors_clean"].apply(lambda x: 1 if actor in x else 0)
all_directors=pd.Series([d for i in movies["director_clean"]for d in i])
top_directors=all_directors.value_counts().head(10).index
for director in top_directors:
    movies[director]=movies["director_clean"].apply(lambda x: 1 if x==director else 0)
movies["overview_len"]=movies["overview"].apply(lambda x: len(str(x).split()))
feature_columns=list(all_genres)+list(top_actors)+list(top_directors)+["overview_len"]
feature_table=movies[["id","title_x"]+feature_columns]
feature_table.to_csv("C:/Users/palak/OneDrive/Desktop/movie_analysis/feature_movie.csv",index=False)
