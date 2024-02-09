import psycopg2

# connect to database
connection = psycopg2.connect(database = "chinook")

# build cursor object of the database
cursor = connection.cursor()


# Add Query 1
cursor.execute('SELECT * FROM "artist"')


# fetch the results multiple
results = cursor.fetchall()

# or fetch results single
# results = cursor.fetchone()

# close the connection 
connection.close()

# print the results
for result in results:
    print(result)