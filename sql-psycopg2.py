import psycopg2

# connect to database
connection = psycopg2.connect(database = "chinook")

# build cursor object of the database
cursor = connection.cursor()


# Add Query 1
#cursor.execute('SELECT * FROM "artist"')
#cursor.execute('SELECT "name" FROM "artist"')
# cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["Queen"])
# cursor.execute('SELECT * FROM "artist" WHERE "artist_id" = %s', [51])
# cursor.execute('SELECT * FROM "album" WHERE "artist_id" = %s', [51])
# cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["Queen"])

cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["ndubz"])


# fetch the results multiple
results = cursor.fetchall()

# or fetch results single
# results = cursor.fetchone()

# close the connection 
connection.close()

# print the results
for result in results:
    print(result)