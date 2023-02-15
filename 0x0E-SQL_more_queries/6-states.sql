-- creates the database hbtn_0d_usa and the table states
-- table has id and name where id is a PK and name cannot be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (`id` INT AUTO_INCREMENT PRIMARY KEY, `name` VARCHAR(256) NOT NULL);
