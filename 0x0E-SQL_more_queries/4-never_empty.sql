-- creates a table with id  not null
-- id and name
-- will not fail if it already exists

CREATE TABLE IF NOT EXISTS id_not_null (
       id INT DEFAULT 1,
       name VARCHAR(256)
);
