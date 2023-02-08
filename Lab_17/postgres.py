import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="tema16_2",
    user="postgres",
    password=""
)

c = conn.cursor()

c.execute('SELECT VERSION()')
db = c.fetchone()
print('Database version', db)
c.close()


