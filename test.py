
import mysql.connector
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Jenny152!",
    database="sys",
)
cursor = db.cursor()
cursor.execute(
    "SELECT name FROM sys.cocktail WHERE hashtag1 = 'classic'OR hashtag2 = 'summertime';")
result = cursor.fetchall()
print(result[0])
