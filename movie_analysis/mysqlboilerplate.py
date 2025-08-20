import mysql.connector

def run_query(query,values=None):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="palak1503",
        database="movie_recommender"
    )
    cursor = mydb.cursor()
    if values:
        cursor.execute(query,values)
    else:
        cursor.execute(query)
    if query.strip().lower().startswith("select"):
        result=cursor.fetchall()
        cursor.close()
        mydb.close()
        return result 
    mydb.commit()
    cursor.close()
    mydb.close()
    print("query executed")

