-- Write a script that converts hbtn_0c_0 database to UTF8 
-- You need to convert all of the following to UTF8:
-- Database hbtn_0c_0
-- Table first_table
-- Field name in first_table
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;

USE DATABASE hbtn_0c_0;

CREATE table IF NOT EXISTS first_table(`name` VARCHAR(255));

ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table MODIFY name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
