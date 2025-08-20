from mysqlboilerplate import run_query
run_query("""CREATE TABLE IF NOT EXISTS movies(
             movie_id INT PRIMARY KEY,
             title VARCHAR(255),
             release_year INT,
             rating FLOAT,
             overview TEXT)""")
run_query("""CREATE TABLE IF NOT EXISTS generes(
             id INT AUTO_INCREMENT PRIMARY KEY,
             movie_id INT,
             genre VARCHAR(100),
             FOREIGN KEY (movie_id) REFERENCES movies(movie_id))""")
run_query("""CREATE TABLE IF NOT EXISTS actors(
             id INT AUTO_INCREMENT PRIMARY KEY,
             movie_id INT,
             actor_name VARCHAR(255),
             FOREIGN KEY (movie_id) REFERENCES movies(movie_id))""")
run_query("""CREATE TABLE IF NOT EXISTS crew(
             id INT AUTO_INCREMENT PRIMARY KEY,
             movie_id INT,
             director_name VARCHAR(255),
             FOREIGN KEY(movie_id) REFERENCES movies(movie_id))""")
print("tables created successfully")
