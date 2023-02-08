import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="tema17",
    user="postgres",
    password="hAv3eleFant77@%$"
)

c = conn.cursor()

#17_3.a

c.execute("""
select id from student;
""")

last_id = len(c.fetchall())

print(f"There are {last_id} student(s).")

#17_3.b

c.execute(
    """
select id from student s where s.last_name = 'Pop';
"""
)

num_of_pop = len(c.fetchall()[-1])

print(f"There are {num_of_pop} student(s) with the last name Pop.")

#17_3.c

c.execute("""
select
	s.first_name
from
	student s, class c
where
	s.class_id = c.id and concat(c.class_number, c.class_letter) = '10f'
order by s.last_name asc;""")

li = len(c.fetchall())

print(f'There are {li} students in class 10f.')

c.close()