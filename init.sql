CREATE USER 'test_user'@'localhost' IDENTIFIED BY 'Auth@123';

CREATE DATABASE auth;

GRANT ALL PRIVILEGES ON auth.* TO 'test_user'@'localhost';

USE auth;

CREATE TABLE user (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

INSERT INTO user (email, password) VALUES ('test@gmail.com', '123');