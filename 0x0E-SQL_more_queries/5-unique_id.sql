-- creates the table unique_id on your MySQL server.
-- table has an id and name where id must be unique
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
