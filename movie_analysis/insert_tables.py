import pandas as pd
from mysqlboilerplate import run_query
import ast
movies=pd.read_csv("C:/Users/palak/OneDrive/Desktop/movie_analysis/clean_movies.csv")
for i,r in movies.iterrows():
    run_query("""INSERT INTO movies(movie_id,title,release_year,rating,overview)
                 VALUES(%s,%s,%s,%s,%s)ON DUPLICATE KEY UPDATE title=VALUES(title)""",
                 (int(r["id"]),r["title_x"],int(r["release_year"])if not pd.isna(r["release_year"])else None,float(r["vote_average"])if not pd.isna(r["vote_average"])else None,r["overview"]if not pd.isna(r["overview"])else None))
    if pd.notna(r["genres_clean"]):
        genres_list = ast.literal_eval(r["genres_clean"]) if isinstance(r["genres_clean"], str) else r["genres_clean"]
        for g in genres_list:
            run_query("""INSERT INTO generes(movie_id,genre) VALUES (%s,%s)""", (int(r["id"]), g))
    if pd.notna(r["actors_clean"]):
        actors_list = ast.literal_eval(r["actors_clean"]) if isinstance(r["actors_clean"], str) else r["actors_clean"]
        for a in actors_list:
            run_query("""INSERT INTO actors(movie_id,actor_name) VALUES (%s,%s)""", (int(r["id"]), a))
        if pd.notna(r["director_clean"]):
            run_query("""INSERT INTO crew(movie_id,director_name)VALUES(%s,%s)""",(int(r["id"]),r["director_clean"]))
print("data inserted")
