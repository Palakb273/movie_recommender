Movie Analysis Project
📌 Introduction

This project analyzes a movie dataset stored in MySQL, focusing on:

Most popular genres

Most frequent actors

Distribution of movie ratings

The analysis is done using Python (Pandas, Matplotlib, Seaborn) and visualized through bar charts and histograms.

⚙️ Tech Stack

Python 3.10+

MySQL (for storing and querying data)

Libraries:

Pandas

Matplotlib

Seaborn

mysql-connector-python / mysqlboilerplate
🚀 Setup & Usage

Clone the Repository

git clone https://github.com/Palakb273/movie_recommender.git
cd movie_analysis


Install Dependencies

pip install -r requirements.txt


Configure Database Connection
Update run_query function (in data.py) with your MySQL credentials.

Run the Analysis

python data.py


View Outputs
Plots will be saved in the plots/ folder:

📊 Top 10 Movie Genres → plots/top_genres.png

🎭 Top 10 Actors → plots/top_actors.png

⭐ Rating Distribution → plots/rating_distribution.png

📊 Sample Outputs
Top 10 Movie Genres 

<img width="1197" height="780" alt="image" src="https://github.com/user-attachments/assets/8101516b-1d95-46e3-89c8-74f01cc663b8" />


Top 10 Actors

<img width="1255" height="754" alt="image" src="https://github.com/user-attachments/assets/d9dfc6a6-456b-4e3f-8acc-6fc7d80882dd" />


Distribution of Ratings

<img width="998" height="745" alt="image" src="https://github.com/user-attachments/assets/cc53a112-3757-47c4-abba-734a953cdea8" />


📌 Future Improvements

Add director-wise analysis

Explore revenue/box office insights

Build interactive dashboards with Plotly/Streamlit
