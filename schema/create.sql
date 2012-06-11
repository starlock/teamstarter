CREATE SEQUENCE users_id_seq;

CREATE TABLE users (
    id INT NOT NULL UNIQUE DEFAULT NEXTVAL('users_id_seq'),
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
