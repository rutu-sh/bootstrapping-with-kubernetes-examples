-- create_database_and_table_with_inserts.sql

CREATE DATABASE IF NOT EXISTS demo_db;

USE demo_db;

CREATE TABLE IF NOT EXISTS users (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(30),
    email VARCHAR(30),
    age INT,
    created_at DATETIME,
    updated_at DATETIME
);

-- Sample insert statements
INSERT INTO users (id, name, email, age, created_at, updated_at) VALUES ('59826e90-861e-4c5f-bc2f-de8ecdca45ee', 'John Doe', 'john.doe@example.com', 30, NOW(), NOW());
INSERT INTO users (id, name, email, age, created_at, updated_at) VALUES ('e31db988-3015-46d4-8e63-16e6134c81c9', 'Adam Smith', 'adam.smith@example.com', 25, NOW(), NOW());
INSERT INTO users (id, name, email, age, created_at, updated_at) VALUES ('efc4aabf-dd57-42b0-b7ef-7dc29cb8c832', 'Will White', 'will.white@example.com', 24, NOW(), NOW());
INSERT INTO users (id, name, email, age, created_at, updated_at) VALUES ('54b49005-34f0-41b0-b505-96c5038e556a', 'April Grey', 'april.grey@example.com', 20, NOW(), NOW());