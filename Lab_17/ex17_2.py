import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="tema17",
    user="postgres",
    password="hAv3eleFant77@%$"
)

c = conn.cursor()

#selects data

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

#fetches data

table = c.fetchall()

#prints to txt doc

with open("Student_Table.txt", "w") as t:
    print('-' * 45, file=t)
    print(f"{'Nume':<20}{'Prenume':<20}{'Clasa':>5}", file=t)
    print('-'*45, file=t)
    for tup in table:
        print(f"{tup[0]:<20}{tup[1]:<20}{tup[2]:>5}", file=t)
    print('-' * 45, file=t)

c.close()