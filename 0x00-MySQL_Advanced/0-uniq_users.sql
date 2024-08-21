-- A script that creates a table users with the following requirements:
-- Attributes: table users with id, email, and name columns
-- id: integer, never null, auto increment, and primary key
-- email: string (255 characters), never null, unique
-- name: string (255 characters)

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL
);
