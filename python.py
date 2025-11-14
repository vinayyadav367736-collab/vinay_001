# DBMS - system DataBase Managemenet

Definition - 
1. A database is an organized collection of structured information,
 or data, stored electronically in a computer system 
 and controlled by a database management system (DBMS).

2. Structured Data: Data is stored in a predefined, tabular format,
 with clear relationships between different data entities.

Common uses of SQL databases:

--> Transactional applications: Managing banking transactions,
 online orders, inventory systems, and patient records.
--> Reporting and analytics: Storing data for business intelligence and data analysis.
-->Web applications: Providing the backend data storage for websites and online services.

# JSON DATABASE::

A JSON database is a type of No SQL document database that stores, retrieves, and manages data in JSON (JavaScript Object Notation) format. Unlike traditional relational databases that use rigid, tabular structures with rows and columns, JSON databases store data as flexible, semi-structured documents. 

key characteristics of JSON databases:

1--> Human-readable and machine-parseable:
2--> NoSQL advantages:\

### USE QUERY

CREATE DATABASE SCHOOL;
USE SCHOOL;

CREATE_TABLE_STUDENTS(
StudentsID varchar(100), Age int, City varchar(100));
# to create a table in SQL, the CREATE TABLE statement is used. This statement defines the structure of a new table in a database, including its name, column names, and their respective data types.
# varchar define table type . store data in string format

Insert Into STUDENTS values (("Rachit",19,"Gurugram"),("Ritik",12,"Delhi"));
# use insert to insert data into table and use values to input multiple values

("Rachit",19,"Gurugram") # first row
("Ritik",12,"Delhi") # second row

# in primary key insert unique value 
# for output we use SELECT FROM
CREATE TABLE STUDENTS (
STUDENTSID INTEGER PRIMARY KEY,STUDENTSID varchar(100),Age int,City varchar(100));

INSERT INTO STUDENTS VALUES ("Vinay",18,"Rewari");
INSERT INTO STUDENTS VALUES ("Rishi",20,"Gurugram");
INSERT INTO STUDENTS VALUES ("Himanshu",18,"Jaipur");
INSERT INTO STUDENTS VALUES ("Aaditya",15,"Delhi");
INSERT INTO STUDENTS VALUES ("Himesh",12,"Rothak");
INSERT INTO STUDENTS VALUES ("Daksh",23,"Karnal");
INSERT INTO STUDENTS VALUES ("Mohit",21,"Panipat");

SELECT * FROM STUDENTS;

-- desc STUDENTS;

SELECT name FROM STUDENTS;
# update EMPLOYEE set name ="vinay" where empID = 2;
# delete to 
CREATE TABLE EMPLOYEE (
  empId INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  dept TEXT NOT NULL
);

-- insert
INSERT INTO EMPLOYEE VALUES (0001, 'Clark', 'Sales');
INSERT INTO EMPLOYEE VALUES (0002, 'Dave', 'Accounting');
INSERT INTO EMPLOYEE VALUES (0003, 'jack', 'Sales');
INSERT INTO EMPLOYEE VALUES (0004, 'olly', 'Acounting');
INSERT INTO EMPLOYEE VALUES (0005, 'bob', 'Sales');
INSERT INTO EMPLOYEE VALUES (0006, 'avak', 'Accounting');
-- fetch 
-- SELECT * FROM EMPLOYEE WHERE dept = 'Sales';

-- update EMPLOYEE set name='Vinay' where empID = 2;
# delete from EMPLOYEE where empID = 2;
SELECT * FROM EMPLOYEE;

# DDL (DATA DEFINATION LANGUAGE)
1. CREATE
2. ALTER - To Change in the existing table
3. DROP - Remove The Data Base
4. Truncate - Remove the table 

# DML(DATA MANIPULATION LANGUAGE) :: to change the data

1. Select - output The SELECT statement in SQL is considered part 
                    of Data Manipulation Language (DML), although it is also 
                    frequently categorized under Data Query Language (DQL).

2. Update - update  The UPDATE command is a Data Manipulation Language 
                    (DML) statement used to modify existing data in a table

3. Insert - to add    Insert" is a Data Manipulation Language 
                        (DML) command used to add new rows of data into a database table. 

4. Delete - to delete  The DELETE command in SQL is a fundamental 
                        component of Data Manipulation Language (DML). 
                        It is used to remove existing rows from a table in a database. 


# OR NOT 
CREATE TABLE EMPLOYEE (
  empId INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  dept TEXT NOT NULL
);

-- insert
INSERT INTO EMPLOYEE VALUES (0001, 'Clark', 'Sales');
INSERT INTO EMPLOYEE VALUES (0002, 'Dave', 'Accounting');
INSERT INTO EMPLOYEE VALUES (0003, 'jack', 'Teacher');
INSERT INTO EMPLOYEE VALUES (0004, 'olly', 'Acounting');
INSERT INTO EMPLOYEE VALUES (0005, 'bob', 'Teacher');
INSERT INTO EMPLOYEE VALUES (0006, 'avak', 'Student');
-- fetch 
-- SELECT * FROM EMPLOYEE WHERE dept = 'Sales';

-- update EMPLOYEE set name='Vinay' where empID = 2;
-- delete from EMPLOYEE where empID = 2;
-- SELECT * FROM EMPLOYEE;
# SELECT * from EMPLOYEE where NOT empID <002 OR empID > 004;




CREATE TABLE EMPLOYEE (
  empId INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  dept TEXT NOT NULL
);

-- insert
INSERT INTO EMPLOYEE VALUES (0001, 'Clark', 'Sales');
INSERT INTO EMPLOYEE VALUES (0002, 'Dave', 'Accounting');
INSERT INTO EMPLOYEE VALUES (0003, 'jack', 'Teacher');
INSERT INTO EMPLOYEE VALUES (0004, 'olly', 'Acounting');
INSERT INTO EMPLOYEE VALUES (0005, 'bob', 'Teacher');
INSERT INTO EMPLOYEE VALUES (0006, 'avak', 'Student');
-- fetch 
-- SELECT * FROM EMPLOYEE WHERE dept = 'Sales';

-- update EMPLOYEE set name='Vinay' where empID = 2;
-- delete from EMPLOYEE where empID = 2;
-- SELECT * FROM EMPLOYEE;
SELECT * from EMPLOYEE where name like '_o%';

select * from EMPLOYEE limit 4;

select count(*), avg(empId),max(empid),min(empid) from EMPLOYEE;

