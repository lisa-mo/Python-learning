import mysql.connector

my_connection = mysql.connector.connect(
    user="",
    password="",
    host="",
    database=""
)

cursor = my_connection.cursor()

word = input("Enter a word: ")

query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s' " % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[0])
else:
    print("There is no such a word!")