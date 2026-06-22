-- -- creating db
-- create database my_db;


-- -- SQL is not case sensitive so we can write queries in both 


-- -- delete db 
-- drop database my_db;

-- use my_db; 
-- -- mean that from we will do all stuff in this one


-- CREATING TABLE
USE my_db;
CREATE TABLE tbl_name(
    name2_id datatype constrains,
    name2_name datatype constrains,
    name2_age datatype constrains,
);

-- I.E 
CREATE TABLE student(
	id INT PRIMARY KEY,
	name VARCHAR(50),
	age INT NOT NULL
);


-- not to be run again so we selct a specif area and then exe


-- insert valuwss
INSERT INTO student VALUES(1,"JAMAL", 17);
INSERT INTO student VALUES(2,"GHBN", 17);
INSERT INTO student VALUES(3,"BNML", 17);
INSERT INTO student VALUES(4,"JGHJK", 17);
INSERT INTO student VALUES(5,"JAGHJL", 17);
INSERT INTO student VALUES(6,"JARTY", 17);
INSERT INTO student VALUES(7,"JAJ", 17);



-- CHAR(size) 	A FIXED length string (can contain letters, numbers, and special characters). The size parameter specifies the column length in characters - can be from 0 to 255. Default is 1
-- VARCHAR(size) 	A VARIABLE length string (can contain letters, numbers, and special characters). The size parameter specifies the maximum string length in characters - can be from 0 to 65535
-- BINARY(size) 	Equal to CHAR(), but stores binary byte strings. The size parameter specifies the column length in bytes. Default is 1
ete etc etc


-- other here:7unjnjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
https://www.w3schools.com/sql/sql_datatypes.asp




