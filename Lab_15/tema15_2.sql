create database tema15_1;

create table if not exists Student (
	id serial primary key,
	surname varchar(20),
	first_name varchar(20),
	class_nr smallint,
	class_letter varchar(1),
	birth_date date,
	average_grade decimal
);

insert into student (surname,first_name,class_nr,class_letter,birth_date,average_grade
) 
values ('Ionescu', 'Gelu', '5', 'a', '2011-09-02', '7.45');

insert into student (surname,first_name,class_nr,class_letter,birth_date,average_grade
) 
values ('Radulescu', 'Ana-Maria', '10', 'c', '2005-05-11', '8.25');

insert into student (surname,first_name,class_nr,class_letter,birth_date,average_grade
) 
values ('Muresan', 'Ionel', '9', 'a', '2006-12-03', '9.00');

insert into student (surname,first_name,class_nr,class_letter,birth_date,average_grade
) 
values ('Lopez', 'Jennifer', '10', 'c', '1985-10-02', '8.55');

insert into student (surname,first_name,class_nr,class_letter,birth_date,average_grade
) 
values ('Todoran', 'Temistocle', '10', 'a', '1999-06-07', '9.67');

insert into student (surname,first_name,class_nr,class_letter,birth_date,average_grade
) 
values ('Popa', 'Ioana', '6', 'b', '2009-10-06', '8.40');

insert into student (surname,first_name,class_nr,class_letter,birth_date,average_grade
) 
values ('Rebengiuc', 'Victor', '6', 'a', '1977-09-02', '7.45');

insert into student (surname,first_name,class_nr,class_letter,birth_date,average_grade
) 
values ('Tanase', 'Ceorgeta', '8', 'c', '2005-05-11', '8.25');

insert into student (surname,first_name,class_nr,class_letter,birth_date,average_grade
) 
values ('Moldovan', 'Stefan', '8', 'a', '2005-12-03', '9.33');

select surname, first_name, average_grade from student

select surname, first_name, average_grade, class_nr, class_letter from student where class_nr = 10

select surname, first_name, average_grade from student where class_nr = 10 and class_letter = 'c'

select surname, first_name, average_grade from student order by surname asc

select surname, first_name, average_grade from student order by average_grade desc

select surname, first_name, average_grade from student order by average_grade desc limit 3

select birth_date, surname, first_name from student where birth_date between '2005-01-01' and '2005-12-31'

alter table student add column school_type varchar(20);

update student set school_type = 'Highschool' where average_grade >= 9

update student set school_type = 'Gymnasium' where average_grade <= 8