-- A script that creates a table users with the following requirements:
-- id, integer, never null, auto increment and primary key
-- email, string (255 characters), never null and unique
-- name, string (255 characters)
-- country, enumeration of countries: US, CO and TN, never null 
-- (= default will be the first element of the enumeration, here US)
-- if table already exists, script should not fail

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);