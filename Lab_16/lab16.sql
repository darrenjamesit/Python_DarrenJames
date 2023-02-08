create table grade (
	id serial,
	description varchar(100) null,
	constraint grade_pk primary key (id)
);

create table student (
	id serial,
	surname varchar(20) not null,
	first_name varchar(20) null,
	class_nr int,
	grade_id int,
	constraint student_pk primary key (id),
	constraint fk_grade
		foreign key (grade_id)
			references grade(id)
); 

create table class_name (
	id serial,
	class_nr int not null,
	student_id int,
	constraint class_pk primary key (id)
); 

alter table class_name add constraint fk_student
		foreign key (student_id)
			references student(id);

		
ALTER TABLE class_name  DROP COLUMN student_id;

ALTER TABLE class_name  DROP constraint fk_student;

alter table class_name alter column class_nr type varchar(20);
