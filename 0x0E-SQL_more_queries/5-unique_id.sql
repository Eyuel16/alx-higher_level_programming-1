-- creates a script
-- named unique_id
-- will not fail if it already exists

CREATE TABEL IF NOT EXISTS unique_id (
       id INT  DEFAULT 1 UNIQUE,
       name VARCHAR(256)
);
