CREATE TABLE Student(
    s_id VARCHAR(20),
    s_name VARCHAR(20) NOT NULL DEFAULT '',
    s_birth VARCHAR(20) NOT NULL DEFAULT '',
    s_sex VARCHAR(10) NOT NULL DEFAULT '',
    PRIMARY KEY(s_id)
);

insert into
    Student
values
('01', 'Zhao Lei', '1990-01-01', 'Male');

insert into
    Student
values
('02', 'Qian Dian', '1990-12-21', 'Male');

insert into
    Student
values
('03', 'Sun Feng', '1990-05-20', 'Male');

insert into
    Student
values
('04', 'Li Yun', '1990-08-06', 'Male');

insert into
    Student
values
('05', 'Zhou Mei', '1991-12-01', 'Female');

insert into
    Student
values
('06', 'Wu Lan', '1992-03-01', 'Female');

insert into
    Student
values
('07', 'Zheng Zhu', '1989-07-01', 'Female');

insert into
    Student
values
('08', 'Wang Ju', '1990-01-20', 'Female');