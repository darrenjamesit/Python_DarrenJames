import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="tema17",
    user="postgres",
    password="hAv3eleFant77@%$"
)

c = conn.cursor()

c.execute("""
select
	s.last_name as "Nume",
	s.first_name as "Prenume",
	concat(c.class_number, c.class_letter) as "Clasa"
from
	student s, class c
where
	s.class_id = c.id
order by s.last_name asc;""")

table = c.fetchall()
print(table)

c.close()


